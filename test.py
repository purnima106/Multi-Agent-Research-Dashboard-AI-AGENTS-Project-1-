import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from app.services.web_scraper import WebScraper

scraper = WebScraper(num_results=2)
results = scraper.get_articles_content("AI in medical diagnostics")

for i, article in enumerate(results):
    print(f"\nArticle {i+1}: {article['url']}")
    print(article['content'][:500])  # Print first 500 chars only
