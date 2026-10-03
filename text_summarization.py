import argparse
from pathlib import Path


def summarize_text(text):
    """Summarize text, adapting output limits for short transcripts."""
    if not text.strip():
        raise ValueError("Cannot summarize empty text.")

    from transformers import pipeline

    word_count = len(text.split())
    max_length = min(150, max(8, word_count))
    min_length = min(50, max(1, max_length // 3))
    summarizer = pipeline("summarization")
    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False,
        truncation=True,
    )
    return summary[0]["summary_text"]


def main():
    parser = argparse.ArgumentParser(description="Summarize a meeting transcript.")
    parser.add_argument("transcript", type=Path, help="Path to a UTF-8 transcript")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("summary.txt"),
        help="Output path (default: summary.txt)",
    )
    args = parser.parse_args()

    summary = summarize_text(args.transcript.read_text(encoding="utf-8"))
    args.output.write_text(summary, encoding="utf-8")
    print(f"Summary saved to: {args.output}")


if __name__ == "__main__":
    main()
