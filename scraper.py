"""
Web scraper for news websites and RSS feeds
"""
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from urllib.parse import urljoin, urlparse
import time
import feedparser
from datetime import datetime
from config import NEWS_SOURCES, COMMON_SELECTORS, SCRAPER_CONFIG

class NewsScraper:
    def __init__(self):
        self.config = SCRAPER_CONFIG
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        headers = {"User-Agent": self.config["user_agent"]}
        self.session = aiohttp.ClientSession(
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=self.config["timeout"])
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def fetch_page(self, url: str) -> Optional[str]:
        """Fetch HTML content from URL"""
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    print(f"Error fetching {url}: Status {response.status}")
                    return None
        except asyncio.TimeoutError:
            print(f"Timeout fetching {url}")
            return None
        except Exception as e:
            print(f"Exception fetching {url}: {str(e)}")
            return None
    
    def extract_article_links(self, html: str, source_config: Dict) -> List[str]:
        """Extract article links from homepage"""
        soup = BeautifulSoup(html, 'lxml')
        selectors = source_config.get("selectors", COMMON_SELECTORS)
        link_selector = selectors.get("article_links", "a")
        
        links = []
        base_url = source_config["url"]
        base_domain = urlparse(base_url).netloc
        
        for link in soup.select(link_selector):
            href = link.get('href')
            if href:
                # Convert relative URLs to absolute
                full_url = urljoin(base_url, href)
                # Only include URLs from the same domain
                if urlparse(full_url).netloc == base_domain:
                    links.append(full_url)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_links = []
        for link in links:
            if link not in seen:
                seen.add(link)
                unique_links.append(link)
        
        return unique_links[:self.config["max_articles_per_site"]]
    
    def extract_article_content(self, html: str, source_config: Dict) -> Dict[str, Optional[str]]:
        """Extract article title, content, and date"""
        soup = BeautifulSoup(html, 'lxml')
        selectors = source_config.get("selectors", COMMON_SELECTORS)
        
        # Extract title
        title = None
        title_selectors = [
            selectors.get("title"),
            "h1",
            ".article-title",
            ".post-title",
            ".headline",
            "title"
        ]
        for selector in title_selectors:
            if selector:
                element = soup.select_one(selector)
                if element:
                    title = element.get_text(strip=True)
                    if title and len(title) > 5:  # Ensure meaningful title
                        break
        
        # Extract content
        content = None
        content_selectors = [
            selectors.get("content"),
            "article",
            "main",
            ".content",
            ".article-content",
            ".post-content",
            ".entry-content"
        ]
        for selector in content_selectors:
            if selector:
                element = soup.select_one(selector)
                if element:
                    # Remove script and style elements
                    for script in element(["script", "style", "nav", "footer", "header", "aside"]):
                        script.decompose()
                    content = element.get_text(separator="\n", strip=True)
                    if len(content) > 100:  # Ensure we have substantial content
                        break
        
        # Extract date
        date = None
        date_selectors = [
            selectors.get("date"),
            "time",
            ".date",
            ".published-date",
            ".article-date",
            "[datetime]"
        ]
        for selector in date_selectors:
            if selector:
                element = soup.select_one(selector)
                if element:
                    date = element.get('datetime') or element.get_text(strip=True)
                    if date:
                        break
        
        return {
            "title": title or "No title found",
            "content": content or "",
            "date": date
        }
    
    async def scrape_rss_feed(self, source_config: Dict) -> List[Dict]:
        """Scrape articles from an RSS feed"""
        feed_url = source_config["url"]
        
        try:
            # Fetch RSS feed
            feed_content = await self.fetch_page(feed_url)
            if not feed_content:
                return []
            
            # Parse RSS feed
            feed = feedparser.parse(feed_content)
            
            if feed.bozo and feed.bozo_exception:
                print(f"RSS parsing error for {source_config['name']}: {feed.bozo_exception}")
                return []
            
            articles = []
            max_articles = self.config.get("max_articles_per_site", 50)
            
            for entry in feed.entries[:max_articles]:
                # Extract article data from RSS entry
                title = entry.get("title", "No title")
                link = entry.get("link", "")
                
                # Get content - try different fields
                content = ""
                if "content" in entry:
                    content = entry.content[0].value if isinstance(entry.content, list) else str(entry.content)
                elif "summary" in entry:
                    content = entry.summary
                elif "description" in entry:
                    content = entry.description
                
                # Get published date
                published_date = None
                if "published_parsed" in entry and entry.published_parsed:
                    try:
                        published_date = datetime(*entry.published_parsed[:6]).isoformat()
                    except:
                        pass
                elif "published" in entry:
                    published_date = entry.published
                
                # Clean HTML from content if present
                if content:
                    soup = BeautifulSoup(content, 'html.parser')
                    content = soup.get_text(separator="\n", strip=True)
                
                if title and link:
                    articles.append({
                        "url": link,
                        "source": source_config["name"],
                        "title": title,
                        "content": content,
                        "date": published_date
                    })
            
            return articles
            
        except Exception as e:
            print(f"Error parsing RSS feed {source_config['name']}: {str(e)}")
            return []
    
    async def scrape_source(self, source_config: Dict) -> List[Dict]:
        """Scrape articles from a single news source (RSS or HTML)"""
        print(f"Scraping {source_config['name']}...")
        
        # Check if this is an RSS feed
        is_rss = source_config.get("is_rss", False)
        
        # Auto-detect RSS feeds by URL pattern
        if not is_rss:
            url_lower = source_config["url"].lower()
            is_rss = any(pattern in url_lower for pattern in [
                "/feed", "/rss", ".xml", ".atom", "feedburner", "feeds."
            ])
        
        if is_rss:
            articles = await self.scrape_rss_feed(source_config)
            print(f"Found {len(articles)} articles from RSS feed: {source_config['name']}")
            return articles
        
        # Otherwise, scrape HTML
        # Fetch homepage
        html = await self.fetch_page(source_config["url"])
        if not html:
            return []
        
        # Extract article links
        article_links = self.extract_article_links(html, source_config)
        print(f"Found {len(article_links)} articles on {source_config['name']}")
        
        # Scrape each article
        articles = []
        for i, link in enumerate(article_links):
            if i > 0:
                await asyncio.sleep(self.config["request_delay"])
            
            article_html = await self.fetch_page(link)
            if article_html:
                content = self.extract_article_content(article_html, source_config)
                if content.get("content"):  # Only add if we got content
                    articles.append({
                        "url": link,
                        "source": source_config["name"],
                        **content
                    })
        
        return articles
    
    async def scrape_all_sources(self, sources: List[Dict]) -> List[Dict]:
        """Scrape all news sources with concurrency control"""
        all_articles = []
        
        # Process sources in batches to avoid overwhelming servers
        batch_size = self.config.get("concurrent_sources", 10)
        batch_delay = self.config.get("batch_delay", 5.0)
        
        for i in range(0, len(sources), batch_size):
            batch = sources[i:i + batch_size]
            print(f"\nProcessing batch {i//batch_size + 1} ({len(batch)} sources)...")
            
            tasks = [self.scrape_source(source) for source in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                if isinstance(result, Exception):
                    print(f"Error scraping {batch[j]['name']}: {str(result)}")
                else:
                    all_articles.extend(result)
            
            # Delay between batches
            if i + batch_size < len(sources):
                print(f"Waiting {batch_delay} seconds before next batch...")
                await asyncio.sleep(batch_delay)
        
        return all_articles


