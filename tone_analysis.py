import argparse
from pathlib import Path


def analyze_tone(text):
    """Categorize the tone using a small set of keyword rules."""
    if not text.strip():
        raise ValueError("Cannot analyze tone of empty text.")

    text = text.casefold()
    if "urgent" in text or "immediately" in text:
        return "Fast-paced and urgent"
    if "discussion" in text or "meeting" in text:
        return "Professional"
    return "Casual"


def main():
    parser = argparse.ArgumentParser(description="Analyze the tone of a transcript.")
    parser.add_argument("transcript", type=Path, help="Path to a UTF-8 transcript")
    args = parser.parse_args()

    if not args.transcript.is_file():
        raise FileNotFoundError(f"Transcript file not found: {args.transcript}")

    tone = analyze_tone(args.transcript.read_text(encoding="utf-8"))
    print(f"Tone Analysis: {tone}")


if __name__ == "__main__":
    main()
