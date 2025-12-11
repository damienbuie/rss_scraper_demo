# News Scraper with AI Analysis

A powerful news scraping system that uses the OpenAI Agents framework to analyze and filter articles based on your areas of interest. This system can scrape up to 250 news websites and intelligently identify relevant content.

## Features

- **Multi-source scraping**: Scrape 232+ news sources (RSS feeds and websites)
- **RSS feed support**: Automatic detection and parsing of RSS/Atom feeds
- **AI-powered analysis**: Uses OpenAI Agents framework to analyze article relevance
- **Intelligent filtering**: Automatically identifies articles matching your areas of interest
- **Database storage**: SQLite database for efficient article storage and deduplication
- **Daily updates**: Ready for scheduled daily runs
- **Rate limiting**: Respectful scraping with configurable delays

## Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- Internet connection

### Step-by-Step Setup

#### 1. Clone or Navigate to the Project

```bash
cd /path/to/Test
```

#### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
# .venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt when activated.

#### 3. Install Dependencies

```bash
# Make sure virtual environment is activated
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- `openai-agents` - OpenAI Agents framework
- `feedparser` - RSS feed parsing
- `aiohttp` - Async HTTP requests
- `beautifulsoup4` - HTML parsing
- `aiosqlite` - Async SQLite database
- And other dependencies

#### 4. Configure OpenAI API Key

Create a `.env` file in the project root:

```bash
# Create .env file
touch .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Important**: Never commit the `.env` file to version control. It's already in `.gitignore`.

#### 5. Verify Installation

Test that everything is set up correctly:

```bash
# Test imports
python3 -c "from config import NEWS_SOURCES; print(f'✓ {len(NEWS_SOURCES)} sources loaded')"
python3 -c "from agent_analyzer import NewsAnalyzer; print('✓ Agent analyzer ready')"
python3 -c "from scraper import NewsScraper; print('✓ Scraper ready')"
```

#### 6. (Optional) Customize Configuration

Edit `config.py` to:
- Adjust `AREAS_OF_INTEREST` to match your specific topics
- Modify `SCRAPER_CONFIG` for rate limiting and timeouts
- Adjust `AGENT_CONFIG` for model selection and relevance thresholds

**Note**: The system comes pre-configured with 232 news sources focused on security, intelligence, and disinformation. You can modify these in `config.py` if needed.

#### 7. Run Your First Scrape

```bash
# Make sure virtual environment is activated
python main.py
```

The script will:
1. Scrape all configured news sources
2. Check for new articles (skip duplicates)
3. Analyze articles with AI for relevance
4. Save relevant articles to the database
5. Display a summary of results

**First run tip**: Consider testing with a smaller subset first by temporarily limiting `NEWS_SOURCES` in `config.py` to just a few sources.

### Quick Start (TL;DR)

```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up API key
echo "OPENAI_API_KEY=your_key_here" > .env

# 4. Run scraper
python main.py
```

## Configuration

### Areas of Interest

Edit `AREAS_OF_INTEREST` in `config.py` to specify what topics you're interested in:

```python
AREAS_OF_INTEREST = [
    "artificial intelligence",
    "machine learning",
    "climate change",
    # ... add your topics
]
```

### News Sources

The system includes 232 pre-configured news sources focused on security, intelligence, and disinformation. Sources are configured in `NEWS_SOURCES` in `config.py`.

For RSS feeds (most sources):
```python
{
    "name": "Source Name",
    "url": "https://example.com/feed/",
    "is_rss": True,
    "selectors": {}
}
```

For HTML websites:
```python
{
    "name": "Source Name",
    "url": "https://example.com",
    "is_rss": False,
    "selectors": {
        "article_links": "CSS selector for article links",
        "title": "CSS selector for article title",
        "content": "CSS selector for article content",
        "date": "CSS selector for publication date"
    }
}
```

RSS feeds are automatically detected by URL patterns (containing `/feed`, `/rss`, `.xml`, etc.), but you can explicitly set `is_rss: True/False`.

### Scraper Settings

Adjust `SCRAPER_CONFIG` in `config.py`:

- `max_articles_per_site`: Maximum articles to scrape per site per run
- `request_delay`: Seconds between requests (be respectful!)
- `timeout`: Request timeout in seconds
- `concurrent_sources`: Number of sources to scrape concurrently
- `batch_delay`: Delay between batches of concurrent requests
- `max_sources`: Limit how many sources to process (e.g., 50). Set to `None` to use all.

### Agent Settings

Adjust `AGENT_CONFIG` in `config.py`:

- `model`: OpenAI model to use (`gpt-4o-mini` for cost efficiency, `gpt-4o` for better analysis)
- `relevance_threshold`: Minimum score (0.0-1.0) to consider article relevant
- `max_content_length`: Maximum characters to send to agent (affects token usage)

## Database

The system uses SQLite to store articles. The database includes:

- **articles**: All scraped articles with metadata
- **scraping_log**: Log of each scraping run

### Viewing Articles

Use the provided `view_articles.py` script to view what's in your database:

```bash
# Show statistics and top articles
python view_articles.py

# Show only statistics
python view_articles.py stats

# Show top 20 most relevant articles
python view_articles.py top 20

# Show all articles (up to 50)
python view_articles.py all 50

# Show articles above a relevance threshold
python view_articles.py relevant 0.7 30

# Show articles from a specific source
python view_articles.py source "BBC News - World"
```

### Querying Articles Programmatically

You can also query the database directly using Python:

```python
from database import NewsDatabase
import asyncio

async def get_relevant_articles():
    db = NewsDatabase()
    await db.initialize()
    articles = await db.get_relevant_articles(limit=50, min_relevance=0.7)
    return articles

asyncio.run(get_relevant_articles())
```

### Querying with SQLite

You can also query the database directly using SQLite:

```bash
# Count total articles
sqlite3 news_articles.db "SELECT COUNT(*) FROM articles;"

# View recent articles
sqlite3 news_articles.db "SELECT title, source, relevance_score, scraped_date FROM articles ORDER BY scraped_date DESC LIMIT 10;"

# View top relevant articles
sqlite3 news_articles.db "SELECT title, source, relevance_score FROM articles WHERE relevance_score >= 0.7 ORDER BY relevance_score DESC LIMIT 10;"
```

## Database Analysis (view_articles.py)

Use the bundled viewer to inspect what was scraped and scored:

```bash
# Show stats and top relevant articles (default)
python view_articles.py

# Only statistics
python view_articles.py stats

# Top N most relevant
python view_articles.py top 20

# All articles (no relevance filter)
python view_articles.py all 50

# Articles above a relevance threshold
python view_articles.py relevant 0.7 30

# Articles from a specific source
python view_articles.py source "Science Feedback"
```

What it shows:
- Totals and relevance counts
- Articles by source
- Recent scraping runs
- Titles, source, relevance score, areas, summary (truncated), URL, scraped date

## Scheduling Daily Updates

### Using cron (Linux/Mac)

**Important**: Make sure to use the full path to your Python interpreter and activate the virtual environment.

```bash
# Edit crontab
crontab -e

# Add this line to run daily at 6 AM
# Replace /path/to/project with your actual project path
0 6 * * * cd /path/to/project && /path/to/project/.venv/bin/python /path/to/project/main.py >> /path/to/project/scraper.log 2>&1
```

To find your Python path:
```bash
which python3  # or
.venv/bin/python --version
```

### Using schedule library

Create a file `scheduler.py`:

```python
import schedule
import time
import asyncio
import os
from main import run_daily_update

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

def job():
    print(f"Running scheduled scrape at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        asyncio.run(run_daily_update())
        print("Scrape completed successfully")
    except Exception as e:
        print(f"Error during scheduled scrape: {e}")

# Schedule daily at 6 AM
schedule.every().day.at("06:00").do(job)

# Or schedule every 12 hours
# schedule.every(12).hours.do(job)

print("Scheduler started. Waiting for scheduled time...")
while True:
    schedule.run_pending()
    time.sleep(60)
```

Run the scheduler:
```bash
python scheduler.py
```

### Using systemd (Linux)

Create `/etc/systemd/system/news-scraper.service`:

```ini
[Unit]
Description=News Scraper Daily Update
After=network.target

[Service]
Type=oneshot
User=your-username
WorkingDirectory=/path/to/project
Environment="PATH=/path/to/project/.venv/bin"
ExecStart=/path/to/project/.venv/bin/python /path/to/project/main.py

[Install]
WantedBy=multi-user.target
```

Create `/etc/systemd/system/news-scraper.timer`:

```ini
[Unit]
Description=Run News Scraper Daily
Requires=news-scraper.service

[Timer]
OnCalendar=daily
OnCalendar=06:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable and start:
```bash
sudo systemctl enable news-scraper.timer
sudo systemctl start news-scraper.timer
```

## Project Structure

```
.
├── main.py              # Main orchestration script - run this to start scraping
├── scraper.py           # Web scraping and RSS feed parsing logic
├── agent_analyzer.py    # AI agent for content analysis using OpenAI Agents
├── database.py          # SQLite database operations and article storage
├── config.py            # Configuration: 232 sources, interest areas, settings
├── requirements.txt     # Python dependencies
├── .env                 # Your API keys (create this, not in git)
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
├── .venv/               # Virtual environment (create this)
├── news_articles.db      # SQLite database (created on first run)
└── README.md            # This file
```

## How It Works

1. **Scraping**: The scraper fetches articles from all configured news sources
2. **Deduplication**: Checks database to avoid re-processing existing articles
3. **AI Analysis**: Uses OpenAI Agents to analyze each new article for relevance
4. **Storage**: Saves articles with relevance scores and identified areas of interest
5. **Reporting**: Displays summary of relevant articles found

## Cost Considerations

- Using `gpt-4o-mini` is more cost-effective for large-scale scraping
- Adjust `max_content_length` to control token usage
- The system only analyzes new articles (deduplication saves costs)
- Consider running during off-peak hours for better API rates

## Legal and Ethical Considerations

- **Respect robots.txt**: Check each site's robots.txt before scraping
- **Rate limiting**: Use appropriate delays between requests
- **Terms of service**: Ensure you comply with each site's ToS
- **Attribution**: Consider how you'll use and attribute the scraped content

## Troubleshooting

### "OPENAI_API_KEY not set"
- Make sure you've created a `.env` file in the project root
- Verify the file contains: `OPENAI_API_KEY=sk-...`
- Check that you're running the script from the project directory
- Try: `python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY')[:10] + '...')"`

### "ModuleNotFoundError" or Import Errors
- Make sure your virtual environment is activated (you should see `(.venv)` in your prompt)
- Reinstall dependencies: `pip install -r requirements.txt`
- Verify Python version: `python3 --version` (should be 3.8+)

### "No articles found"
- For RSS feeds: Check that the feed URL is accessible in a browser
- For HTML sites: Check that your CSS selectors in `config.py` are correct
- Some sites may require JavaScript rendering (consider Selenium/Playwright for those)
- Check network connectivity and firewall settings
- Verify the source URL is correct in `config.py`

### "Rate limit errors" from OpenAI
- Check your OpenAI API quota and billing status
- Reduce `concurrent_sources` in `SCRAPER_CONFIG`
- Increase delays: `request_delay` and `batch_delay`
- Consider using `gpt-4o-mini` instead of `gpt-4o` for cost efficiency

### "Rate limit errors" from websites
- Increase `request_delay` in `SCRAPER_CONFIG` (try 2-3 seconds)
- Reduce `concurrent_sources` (try 5 instead of 10)
- Increase `batch_delay` between batches
- Some sites may block automated requests - check their robots.txt

### "Analysis errors"
- Check your OpenAI API key is valid and has credits
- Try reducing `max_content_length` in `AGENT_CONFIG` if hitting token limits
- Verify the model name in `AGENT_CONFIG` (e.g., `gpt-4o-mini` or `gpt-4o`)
- Check OpenAI API status page for outages

### Database Issues
- If database is locked, make sure no other process is using it
- Delete `news_articles.db` to start fresh (you'll lose stored articles)
- Check file permissions on the database file

### RSS Feed Parsing Errors
- Some RSS feeds may be malformed - check the feed URL in a browser
- Atom feeds are supported but may need different parsing
- FeedBurner and other redirect services should work automatically

### General Issues
- **Check logs**: The script prints detailed error messages
- **Test individual components**: Try importing modules individually
- **Verify network**: Some sources may be blocked by your network/firewall
- **Check Python version**: `python3 --version` should show 3.8 or higher

## Extending the System

- **Add more sources**: Simply add to `NEWS_SOURCES` in `config.py`
- **Custom analysis**: Modify `agent_analyzer.py` to add custom analysis logic
- **Export formats**: Add export functions to save articles in JSON, CSV, etc.
- **Notifications**: Add email/Slack notifications for highly relevant articles
- **Web interface**: Build a dashboard to view and search articles

## License

MIT License - feel free to use and modify as needed.

## Acknowledgments

Built using the [OpenAI Agents Python framework](https://github.com/openai/openai-agents-python).


