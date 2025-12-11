"""
Script to view articles stored in the database
"""
import asyncio
import sys
from database import NewsDatabase

async def view_statistics():
    """Display database statistics"""
    db = NewsDatabase()
    await db.initialize()
    
    stats = await db.get_statistics()
    
    print("=" * 60)
    print("Database Statistics")
    print("=" * 60)
    print(f"Total articles in database: {stats['total_articles']}")
    print(f"Relevant articles (score >= 0.5): {stats['relevant_articles']}")
    print(f"\nArticles by source (top 20):")
    print("-" * 60)
    for source, count in list(stats['articles_by_source'].items())[:20]:
        print(f"  {source}: {count}")
    
    if len(stats['articles_by_source']) > 20:
        print(f"\n  ... and {len(stats['articles_by_source']) - 20} more sources")
    
    print("\n" + "=" * 60)
    print("Recent Scraping Runs (last 10)")
    print("=" * 60)
    for run in stats['recent_runs'][:10]:
        status_icon = "✓" if run['status'] == 'success' else "✗"
        print(f"{status_icon} {run['source']}: {run['articles_new']} new / {run['articles_found']} found ({run['run_date'][:19]})")

async def view_articles(limit=20, min_relevance=0.0, source=None):
    """Display articles from database"""
    db = NewsDatabase()
    await db.initialize()
    
    articles = await db.get_relevant_articles(limit=limit, min_relevance=min_relevance, source=source)
    
    if not articles:
        print("No articles found matching criteria.")
        return
    
    print("=" * 60)
    print(f"Articles (showing {len(articles)} of {limit} requested)")
    print("=" * 60)
    
    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']}")
        if article.get('relevance_score'):
            print(f"   Relevance Score: {article['relevance_score']:.2f}")
        if article.get('areas_of_interest'):
            areas = article['areas_of_interest'] if isinstance(article['areas_of_interest'], str) else article['areas_of_interest']
            if areas:
                print(f"   Areas: {areas}")
        if article.get('summary'):
            summary = article['summary'][:150] + "..." if len(article['summary']) > 150 else article['summary']
            print(f"   Summary: {summary}")
        print(f"   Scraped: {article['scraped_date'][:19] if article.get('scraped_date') else 'N/A'}")
        print(f"   URL: {article['url']}")

async def view_top_relevant(limit=10):
    """Display top relevant articles"""
    print("\n" + "=" * 60)
    print(f"Top {limit} Most Relevant Articles")
    print("=" * 60)
    await view_articles(limit=limit, min_relevance=0.7)

async def main():
    """Main function"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "stats":
            await view_statistics()
        elif command == "top":
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            await view_top_relevant(limit)
        elif command == "all":
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 50
            await view_articles(limit=limit, min_relevance=0.0)
        elif command == "relevant":
            min_score = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
            limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
            await view_articles(limit=limit, min_relevance=min_score)
        elif command == "source":
            if len(sys.argv) < 3:
                print("Usage: python view_articles.py source <source_name>")
                print("Example: python view_articles.py source 'BBC News - World'")
                return
            source_name = " ".join(sys.argv[2:])
            await view_articles(limit=50, source=source_name)
        else:
            print(f"Unknown command: {command}")
            print("\nAvailable commands:")
            print("  stats              - Show database statistics")
            print("  top [limit]        - Show top relevant articles (default: 10)")
            print("  all [limit]        - Show all articles (default: 50)")
            print("  relevant [score] [limit] - Show articles above relevance score (default: 0.5, limit: 20)")
            print("  source <name>      - Show articles from specific source")
    else:
        # Default: show statistics and top articles
        await view_statistics()
        await view_top_relevant(10)

if __name__ == "__main__":
    asyncio.run(main())

