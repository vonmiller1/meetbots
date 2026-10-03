import argparse
from pathlib import Path


def audio_to_text(audio_file_path, model_type="base"):
    """Transcribe an audio file with Whisper."""
    audio_path = Path(audio_file_path)
    if not audio_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    import whisper

    model = whisper.load_model(model_type)
    result = model.transcribe(str(audio_path))
    return result["text"]


def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper.")
    parser.add_argument("audio_file", type=Path, help="Path to an audio file")
    parser.add_argument("--model", default="base", help="Whisper model name")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the transcript; prints to stdout otherwise",
    )
    args = parser.parse_args()

    transcript = audio_to_text(args.audio_file, args.model)
    if args.output:
        args.output.write_text(transcript, encoding="utf-8")
        print(f"Transcript saved to: {args.output}")
    else:
        print(transcript)


if __name__ == "__main__":
    main()
