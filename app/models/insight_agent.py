import os
import requests
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

class InsightAgent:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        self.headers = {
            "Authorization": f"Bearer {hf_token}",
            "Content-Type": "application/json"
        }

    def get_insight(self, text):
        payload = {
            "inputs": text
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                return result[0]["summary_text"]
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Exception occurred: {str(e)}"

    def generate_insights(self, list_of_texts):
        """Take a list of text summaries and return their individual insights"""
        insights = []
        for text in list_of_texts:
            insight = self.get_insight(text)
            insights.append(insight)
        return insights
