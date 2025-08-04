from transformers import pipeline

class ArticleAnalyzer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="Falconsai/text_summarization")
        self.qa = pipeline("question-answering")

    def summarize_text(self, text, max_tokens=1024):
        return self.summarizer(text[:max_tokens])[0]['summary_text']

    def extract_facts(self, text):
        questions = [
            "What is the main topic?",
            "What are the challenges mentioned?",
            "What solution is proposed?",
            "Who are the key contributors?",
            "What results or outcomes are mentioned?"
        ]
        return {
            q: self.qa(question=q, context=text)["answer"]
            for q in questions
        }
