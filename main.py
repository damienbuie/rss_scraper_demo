"""
Main orchestration script for news scraping and analysis
"""
import asyncio
import os
from datetime import datetime
from dotenv import load_dotenv
from scraper import NewsScraper
from agent_analyzer import NewsAnalyzer
from database import NewsDatabase
from config import NEWS_SOURCES, AREAS_OF_INTEREST

# Load environment variables
load_dotenv()

async def main():
    """Main function to orchestrate scraping and analysis"""
    print("=" * 60)
    print("News Scraper with AI Analysis")
    print("=" * 60)
    # Decide how many sources to process (controlled via SCRAPER_CONFIG.max_sources)
    from config import SCRAPER_CONFIG
    max_sources = SCRAPER_CONFIG.get("max_sources")
    sources_to_use = NEWS_SOURCES[:max_sources] if max_sources else NEWS_SOURCES

    print(f"Areas of Interest: {', '.join(AREAS_OF_INTEREST)}")
    print(f"Sources to scrape: {len(sources_to_use)}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Initialize database
    db = NewsDatabase()
    await db.initialize()
    print("Database initialized\n")
    
    # Step 1: Scrape all sources
    print("Step 1: Scraping news sources...")
    print("-" * 60)
    all_articles = []
    
    async with NewsScraper() as scraper:
        all_articles = await scraper.scrape_all_sources(sources_to_use)
    
    print(f"\nTotal articles scraped: {len(all_articles)}")
    
    # Step 2: Filter out existing articles
    print("\nStep 2: Checking for new articles...")
    print("-" * 60)
    new_articles = []
    for article in all_articles:
        exists = await db.article_exists(article["url"], article["title"])
        if not exists:
            new_articles.append(article)
    
    print(f"New articles found: {len(new_articles)}")
    
    if not new_articles:
        print("No new articles to analyze. Exiting.")
        return
    
    # Step 3: Analyze articles with AI agent
    print("\nStep 3: Analyzing articles with AI agent...")
    print("-" * 60)
    analyzer = NewsAnalyzer()
    analyzed_articles = await analyzer.analyze_batch(new_articles, rate_limit=0.5)
    
    # Step 4: Save articles to database
    print("\nStep 4: Saving articles to database...")
    print("-" * 60)
    saved_count = 0
    relevant_count = 0
    
    for article in analyzed_articles:
        saved = await db.save_article(
            url=article["url"],
            title=article["title"],
            content=article.get("content", ""),
            source=article["source"],
            published_date=article.get("date"),
            relevance_score=article.get("relevance_score"),
            areas_of_interest=article.get("areas_of_interest", []),
            summary=article.get("summary")
        )
        if saved:
            saved_count += 1
            if article.get("relevant", False):
                relevant_count += 1
    
    print(f"Saved {saved_count} new articles")
    print(f"Relevant articles: {relevant_count}")
    
    # Step 5: Log scraping run
    for source_config in NEWS_SOURCES:
        source_articles = [a for a in all_articles if a["source"] == source_config["name"]]
        new_source_articles = [a for a in new_articles if a["source"] == source_config["name"]]
        
        await db.log_scraping_run(
            source=source_config["name"],
            articles_found=len(source_articles),
            articles_new=len(new_source_articles),
            status="success"
        )
    
    # Step 6: Display summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    stats = await db.get_statistics()
    print(f"Total articles in database: {stats['total_articles']}")
    print(f"Relevant articles: {stats['relevant_articles']}")
    print(f"Articles by source:")
    for source, count in list(stats['articles_by_source'].items())[:10]:
        print(f"  - {source}: {count}")
    if len(stats['articles_by_source']) > 10:
        print(f"  ... and {len(stats['articles_by_source']) - 10} more sources")
    
    # Get and display top relevant articles
    print("\nTop Relevant Articles (Score >= 0.7):")
    print("-" * 60)
    top_articles = await db.get_relevant_articles(limit=10, min_relevance=0.7)
    for i, article in enumerate(top_articles, 1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']}")
        print(f"   Relevance: {article['relevance_score']:.2f}")
        if article.get('areas_of_interest'):
            print(f"   Areas: {article['areas_of_interest']}")
        print(f"   URL: {article['url']}")
    
    print("\n" + "=" * 60)
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

async def run_daily_update():
    """Function to run daily updates (can be scheduled)"""
    await main()

if __name__ == "__main__":
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY environment variable not set!")
        print("Please set it using: export OPENAI_API_KEY=your_key_here")
        exit(1)
    
    # Run the main function
    asyncio.run(main())


