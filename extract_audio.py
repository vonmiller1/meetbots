import argparse
from pathlib import Path


def extract_audio_from_video(video_file_path, output_audio_path):
    """Extract a video's audio track to an audio file."""
    video_path = Path(video_file_path)
    if not video_path.is_file():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    from moviepy.editor import VideoFileClip

    video = VideoFileClip(str(video_path))
    try:
        if video.audio is None:
            raise ValueError(f"Video has no audio track: {video_path}")
        video.audio.write_audiofile(str(output_audio_path))
    finally:
        video.close()


def main():
    parser = argparse.ArgumentParser(description="Extract audio from a video.")
    parser.add_argument("video_file", type=Path, help="Path to a video file")
    parser.add_argument("output_audio", type=Path, help="Path for the extracted audio")
    args = parser.parse_args()

    extract_audio_from_video(args.video_file, args.output_audio)
    print(f"Audio extracted and saved to: {args.output_audio}")


if __name__ == "__main__":
    main()
