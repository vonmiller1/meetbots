import argparse
from pathlib import Path


def perform_speaker_diarization(audio_file_path, n_speakers=2, output_dir="speaker_segments"):
    """Diarize an audio file and save a file for each detected speaker segment."""
    audio_path = Path(audio_file_path)
    if not audio_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    if n_speakers < 1:
        raise ValueError("n_speakers must be at least 1.")

    from pyAudioAnalysis import audioSegmentation as aS
    from pydub import AudioSegment

    _flags, classes, _ = aS.speaker_diarization(
        str(audio_path), n_speakers=n_speakers, plot_res=False
    )
    if len(classes) == 0:
        raise ValueError(f"No speaker segments were detected in: {audio_path}")

    audio = AudioSegment.from_file(str(audio_path))
    segment_duration = len(audio) / len(classes)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    speaker_segments = {}
    for idx, class_label in enumerate(classes):
        speaker_id = int(class_label) + 1
        start_ms = int(idx * segment_duration)
        end_ms = int((idx + 1) * segment_duration)
        segment = audio[start_ms:end_ms]
        segment_path = output_path / f"speaker_{speaker_id}_{start_ms}_{end_ms}.wav"
        segment.export(str(segment_path), format="wav")
        speaker_segments.setdefault(f"speaker_{speaker_id}", []).append(
            (start_ms / 1000, end_ms / 1000)
        )

    return speaker_segments


def main():
    parser = argparse.ArgumentParser(description="Identify speakers in an audio file.")
    parser.add_argument("audio_file", type=Path, help="Path to an audio file")
    parser.add_argument(
        "--speakers", type=int, default=2, help="Expected number of speakers"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("speaker_segments"),
        help="Directory for extracted speaker audio",
    )
    args = parser.parse_args()

    segments = perform_speaker_diarization(
        args.audio_file, n_speakers=args.speakers, output_dir=args.output_dir
    )
    for speaker, timestamps in segments.items():
        print(f"{speaker}: {timestamps}")


if __name__ == "__main__":
    main()
