from duckduckgo_search import DDGS
from newspaper import Article

class WebScraper:
    def __init__(self, num_results=3):
        self.num_results = num_results

    def search_articles(self, query):
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=self.num_results):
                if 'href' in r:
                    results.append(r['href'])
        return results

    def extract_content(self, url):
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article.text
        except Exception as e:
            print(f"Error processing {url}: {e}")
            return ""

    def get_articles_content(self, query):
        urls = self.search_articles(query)
        articles = []
        for url in urls:
            content = self.extract_content(url)
            if content:
                articles.append({"url": url, "content": content})
        return articles
