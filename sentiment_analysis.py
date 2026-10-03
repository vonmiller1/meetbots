import argparse
from pathlib import Path


def analyze_sentiment(text):
    """Analyze the sentiment of non-empty text."""
    if not text.strip():
        raise ValueError("Cannot analyze sentiment of empty text.")

    from transformers import pipeline

    sentiment_analyzer = pipeline("sentiment-analysis")
    return sentiment_analyzer(text)


def main():
    parser = argparse.ArgumentParser(description="Analyze transcript sentiment.")
    parser.add_argument("transcript", type=Path, help="Path to a UTF-8 transcript")
    args = parser.parse_args()
    sentiment = analyze_sentiment(args.transcript.read_text(encoding="utf-8"))
    print(f"Sentiment Analysis: {sentiment}")


if __name__ == "__main__":
    main()
