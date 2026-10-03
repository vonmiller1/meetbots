import argparse
from pathlib import Path


def classify_meeting(text):
    """Classify the meeting type based on keywords."""
    text = text.casefold()
    if "client" in text or "project update" in text:
        return "Client Meeting"
    if "interview" in text:
        return "Interview"
    if "discussion" in text and "team" in text:
        return "Group Discussion"
    return "General Meeting"


def main():
    parser = argparse.ArgumentParser(description="Classify a meeting transcript.")
    parser.add_argument("transcript", type=Path, help="Path to a UTF-8 transcript")
    args = parser.parse_args()
    text = args.transcript.read_text(encoding="utf-8")
    print(f"Meeting Type: {classify_meeting(text)}")


if __name__ == "__main__":
    main()
