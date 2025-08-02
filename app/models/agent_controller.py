from app.models.research_agent import ResearchAgent
from app.models.summarizer_agent import SummarizerAgent

def run_research_pipeline(topic: str):
    research_agent = Research_Agent()
    summarizer_agent = SummarizerAgent()

    documents = research_agent.fetch_documents(topic)
    summaries = summarizer_agent.summarize(documents)

    return{
        "topic":topic,
        "documents":documents,
        "summaries": summaries
    }


