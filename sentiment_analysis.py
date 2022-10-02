from transformers import pipeline

def analyze_sentiment(text):
    """Analyze sentiment of the given text."""
    sentiment_analyzer = pipeline("sentiment-analysis")
    sentiment = sentiment_analyzer(text)
    return sentiment

if __name__ == "__main__":
    with open("data/text/transcription.txt", "r") as file:
        text = file.read()

    sentiment = analyze_sentiment(text)
    print("Sentiment Analysis: ", sentiment)
