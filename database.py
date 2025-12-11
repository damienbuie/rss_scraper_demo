"""
Database operations for storing scraped articles
"""
import aiosqlite
import asyncio
from datetime import datetime
from typing import List, Dict, Optional
import hashlib

class NewsDatabase:
    def __init__(self, db_path: str = "news_articles.db"):
        self.db_path = db_path
        self._initialized = False
    
    async def initialize(self):
        """Initialize database tables"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT,
                    source TEXT NOT NULL,
                    published_date TEXT,
                    scraped_date TEXT NOT NULL,
                    relevance_score REAL,
                    areas_of_interest TEXT,
                    summary TEXT,
                    hash TEXT UNIQUE NOT NULL,
                    processed BOOLEAN DEFAULT 0
                )
            """)
            
            await db.execute("""
                CREATE TABLE IF NOT EXISTS scraping_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source TEXT NOT NULL,
                    run_date TEXT NOT NULL,
                    articles_found INTEGER,
                    articles_new INTEGER,
                    status TEXT,
                    error_message TEXT
                )
            """)
            
            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_url ON articles(url)
            """)
            
            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_hash ON articles(hash)
            """)
            
            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_scraped_date ON articles(scraped_date)
            """)
            
            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_relevance_score ON articles(relevance_score)
            """)
            
            await db.commit()
        self._initialized = True
    
    def _generate_hash(self, url: str, title: str) -> str:
        """Generate hash for deduplication"""
        content = f"{url}{title}".encode('utf-8')
        return hashlib.md5(content).hexdigest()
    
    async def article_exists(self, url: str, title: str) -> bool:
        """Check if article already exists"""
        if not self._initialized:
            await self.initialize()
        
        article_hash = self._generate_hash(url, title)
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(
                "SELECT 1 FROM articles WHERE hash = ? OR url = ?",
                (article_hash, url)
            ) as cursor:
                row = await cursor.fetchone()
                return row is not None
    
    async def save_article(
        self,
        url: str,
        title: str,
        content: str,
        source: str,
        published_date: Optional[str] = None,
        relevance_score: Optional[float] = None,
        areas_of_interest: Optional[List[str]] = None,
        summary: Optional[str] = None
    ) -> bool:
        """Save article if it doesn't exist"""
        if not self._initialized:
            await self.initialize()
        
        if await self.article_exists(url, title):
            return False
        
        article_hash = self._generate_hash(url, title)
        scraped_date = datetime.now().isoformat()
        areas_str = ",".join(areas_of_interest) if areas_of_interest else None
        
        async with aiosqlite.connect(self.db_path) as db:
            try:
                await db.execute("""
                    INSERT INTO articles 
                    (url, title, content, source, published_date, scraped_date, 
                     relevance_score, areas_of_interest, summary, hash)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    url, title, content, source, published_date, scraped_date,
                    relevance_score, areas_str, summary, article_hash
                ))
                await db.commit()
                return True
            except aiosqlite.IntegrityError:
                return False
    
    async def log_scraping_run(
        self,
        source: str,
        articles_found: int,
        articles_new: int,
        status: str = "success",
        error_message: Optional[str] = None
    ):
        """Log scraping run results"""
        if not self._initialized:
            await self.initialize()
        
        run_date = datetime.now().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO scraping_log 
                (source, run_date, articles_found, articles_new, status, error_message)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (source, run_date, articles_found, articles_new, status, error_message))
            await db.commit()
    
    async def get_relevant_articles(
        self,
        limit: int = 100,
        min_relevance: float = 0.7,
        source: Optional[str] = None
    ) -> List[Dict]:
        """Get articles above relevance threshold"""
        if not self._initialized:
            await self.initialize()
        
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            if source:
                async with db.execute("""
                    SELECT * FROM articles 
                    WHERE relevance_score >= ? AND source = ?
                    ORDER BY scraped_date DESC, relevance_score DESC
                    LIMIT ?
                """, (min_relevance, source, limit)) as cursor:
                    rows = await cursor.fetchall()
                    return [dict(row) for row in rows]
            else:
                async with db.execute("""
                    SELECT * FROM articles 
                    WHERE relevance_score >= ?
                    ORDER BY scraped_date DESC, relevance_score DESC
                    LIMIT ?
                """, (min_relevance, limit)) as cursor:
                    rows = await cursor.fetchall()
                    return [dict(row) for row in rows]
    
    async def get_statistics(self) -> Dict:
        """Get scraping statistics"""
        if not self._initialized:
            await self.initialize()
        
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            # Total articles
            async with db.execute("SELECT COUNT(*) FROM articles") as cursor:
                total_articles = (await cursor.fetchone())[0]
            
            # Relevant articles
            async with db.execute(
                "SELECT COUNT(*) FROM articles WHERE relevance_score >= 0.5"
            ) as cursor:
                relevant_articles = (await cursor.fetchone())[0]
            
            # Articles by source
            async with db.execute("""
                SELECT source, COUNT(*) as count 
                FROM articles 
                GROUP BY source 
                ORDER BY count DESC
            """) as cursor:
                by_source = {row[0]: row[1] for row in await cursor.fetchall()}
            
            # Recent scraping runs
            async with db.execute("""
                SELECT source, run_date, articles_found, articles_new, status
                FROM scraping_log
                ORDER BY run_date DESC
                LIMIT 50
            """) as cursor:
                recent_runs = [dict(row) for row in await cursor.fetchall()]
            
            return {
                "total_articles": total_articles,
                "relevant_articles": relevant_articles,
                "articles_by_source": by_source,
                "recent_runs": recent_runs
            }


