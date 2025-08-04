# 🧠 Multi-Agent Research Dashboard using AI Agents (Streamlit + NLP)

This open-source project lets users input any research topic and generates:
- 🔍 Web-scraped content
- 📝 AI-generated summaries & insights
- 📊 Automatic dashboards (word clouds, keyword bars, sentiment scores)

#Deployment Link: 
https://purnima106-multi-agent-research-dashb-appuistreamlit-app-t8u4lp.streamlit.app/

All powered by Python, LLMs, and Streamlit. No API keys required!

---

## 🚀 Features

- 🌐 Web scraping using DuckDuckGo + Newspaper3k
- 🤖 LLM-based summarization (HuggingFace Transformers)
- 🧠 Keyword & insight extraction
- 📈 Auto-generated dashboards:
  - Word cloud of key terms
  - Top keyword frequency
  - Sentiment analysis metrics
- ✅ Open source & Streamlit Cloud deployable

---

## 🗂️ Project Structure (MVC)

multi_agent_research_dashboard/
│
├── app/
│ ├── services/ # Core logic & processing (scraper, metrics, dashboard)
│ │ ├── web_scraper.py
│ │ ├── metrics_extractor.py
│ │ └── dashboard_generator.py
│ └── ui/
│ └── streamlit_app.py # Main Streamlit frontend
│
├── requirements.txt
├── Dockerfile (optional)
└── README.md

yaml
Copy
Edit

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- Transformers (`pipeline`)
- spaCy, TextBlob
- WordCloud, Matplotlib, Pandas
- Newspaper3k, DuckDuckGo Search
- Docker (optional)

---

## 🔧 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/purnima106/Multi-Agent-Research-Dashboard-AI-AGENTS-Project-1-.git
cd Multi-Agent-Research-Dashboard-AI-AGENTS-Project-1-
2. Set Up Environment
bash
Copy
Edit
python -m venv .venv
.\.venv\Scripts\activate      # On Windows
pip install -r requirements.txt
3. Run the App
bash
Copy
Edit
streamlit run app/ui/streamlit_app.py
🌍 Deployment
This project is fully deployable on Streamlit Community Cloud (no Docker or servers needed).

👉 LIVE DEMO LINK (replace with your actual link)

🙋‍♀️ Author
👩‍💻 Purnima Nahata

If you like this project, don't forget to ⭐️ star the repo!

📄 License
This project is licensed under the MIT License.
