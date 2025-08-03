class ResearchAgent:
    def __init__(self):
        pass

    def fetch_documents(self,topic:str)-> list[str]:
        return[
            f"This is a sample about{topic}.",
            f"This is another sample about{topic}"
        ]