from transformers import pipeline

def analyze_sentiment(texts):
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(texts)