class SummarizerAgent:
    def __init__(self):
        pass

    def summarize(self, documents:list[str])-> list[str]:
        summaries = []
        for doc in documents:
            if len(doc) > 60:
                summary = doc[:60] + "..."
            else:
                summary = doc
            summaries.append(summary)
        return summaries