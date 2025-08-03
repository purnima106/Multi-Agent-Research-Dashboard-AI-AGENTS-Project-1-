from app.models.insight_agent import InsightAgent

agent = InsightAgent()

texts = [
    "Artificial Intelligence is transforming healthcare and enabling better diagnostics.",
    "AI is being used in finance to predict market trends and manage risks efficiently."
]

insights = agent.generate_insights(texts)

print("\nGenerated Insights:")
for idx, i in enumerate(insights, 1):
    print(f"{idx}. {i}")
