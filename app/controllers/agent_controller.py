from app.models.research_agent import ResearchAgent
from app.models.summarizer_agent import SummarizerAgent
from app.models.insight_agent import InsightAgent

def run_research_pipeline(topic: str):
    research_agent = ResearchAgent()
    summarizer_agent = SummarizerAgent()
    insight_agent = InsightAgent()

    documents = research_agent.fetch_documents(topic)
    summaries = summarizer_agent.summarize(documents)
    insights = insight_agent.generate_insights(summaries)

    return{
        "topic":topic,
        "documents":documents,
        "summaries": summaries,
        "insights": insights
    }



