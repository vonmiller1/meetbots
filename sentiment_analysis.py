import argparse
from pathlib import Path


_MAX_SENTIMENT_CHARS = 4000


def analyze_sentiment(text):
    """Analyze the sentiment of non-empty text."""
    if not text.strip():
        raise ValueError("Cannot analyze sentiment of empty text.")

    from transformers import pipeline

    snippet = text.strip()[:_MAX_SENTIMENT_CHARS]
    sentiment_analyzer = pipeline("sentiment-analysis")
    return sentiment_analyzer(snippet)


def main():
    parser = argparse.ArgumentParser(description="Analyze transcript sentiment.")
    parser.add_argument("transcript", type=Path, help="Path to a UTF-8 transcript")
    args = parser.parse_args()

    if not args.transcript.is_file():
        raise FileNotFoundError(f"Transcript file not found: {args.transcript}")

    sentiment = analyze_sentiment(args.transcript.read_text(encoding="utf-8"))
    print(f"Sentiment Analysis: {sentiment}")


if __name__ == "__main__":
    main()
