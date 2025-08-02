class ReasearchAgent:
    def __init__(self):
        pass

    def fetch_docs(self,topic:str)-> list[str]:
        return[
            f"This is a sample about{topic}.",
            f"This is another sample about{topic}"
        ]