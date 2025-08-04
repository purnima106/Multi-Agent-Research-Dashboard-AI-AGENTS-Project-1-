import io
import spacy
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class DashboardGenerator:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def generate_wordcloud(self, text):
        wc = WordCloud(width=800, height=400, background_color="white").generate(text)
        buf = io.BytesIO()
        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        return buf

    def keyword_frequency(self, text):
        doc = self.nlp(text)
        keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
        freq = pd.Series(keywords).value_counts().head(10)
        return pd.DataFrame({'Keyword': freq.index, 'Count': freq.values})

    def sentiment_score(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity, blob.sentiment.subjectivity

    def named_entity_summary(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        df = pd.DataFrame(entities, columns=["Entity", "Type"])
        return df.value_counts().reset_index(name="Count")

    def lda_topics(self, texts, n_topics=3):
        vectorizer = CountVectorizer(stop_words='english')
        X = vectorizer.fit_transform(texts)
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(X)
        topics = []
        for topic in lda.components_:
            words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-5:]]
            topics.append(", ".join(words))
        return topics
