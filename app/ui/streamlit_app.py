import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
from app.services.web_scraper import WebScraper
from app.services.metrics_extractor import ArticleAnalyzer
from app.services.dashboard_generator import DashboardGenerator

st.set_page_config(page_title="AI Research Dashboard", layout="wide")
st.title("🧠 AI-Powered Research Summarizer")

query = st.text_input("Enter your research topic:")

if st.button("Summarize"):
    with st.spinner("🔎 Fetching and analyzing articles..."):
        scraper = WebScraper(num_results=2)
        analyzer = ArticleAnalyzer()
        dashboard = DashboardGenerator()

        articles = scraper.get_articles_content(query)

        if not articles:
            st.error("❌ No articles found.")
        else:
            for i, article in enumerate(articles):
                st.markdown(f"## 🔗 Article {i+1}: [{article['url']}]({article['url']})")

                summary = analyzer.summarize_text(article['content'])
                st.markdown("### 📄 Summary")
                st.write(summary)

                insights = analyzer.extract_facts(article['content'])
                st.markdown("### 📌 Key Insights")
                for q, a in insights.items():
                    st.markdown(f"- **{q}**: {a}")

                with st.expander("📚 Full Article Content"):
                    st.write(article['content'])

                st.markdown("### 📊 AI-Generated Dashboard")

                # Word Cloud
                st.markdown("#### ☁️ Word Cloud")
                img_buf = dashboard.generate_wordcloud(article['content'])
                st.image(img_buf, caption="Word Cloud of Key Terms")

                # Top Keywords Bar Chart
                st.markdown("#### 🔠 Top Keywords")
                df_keywords = dashboard.keyword_frequency(article['content'])
                st.bar_chart(df_keywords.set_index("Keyword"))

                # Sentiment Metrics
                st.markdown("#### ❤️ Sentiment Metrics")
                polarity, subjectivity = dashboard.sentiment_score(article['content'])
                col1, col2 = st.columns(2)
                col1.metric("Polarity", f"{polarity:.2f}")
                col2.metric("Subjectivity", f"{subjectivity:.2f}")

                # Named Entities Table
                st.markdown("#### 🧾 Named Entities")
                entity_df = dashboard.named_entity_summary(article['content'])
                st.dataframe(entity_df)

                st.divider()
