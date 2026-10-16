# MeetSummarizer (meetbots)

Python command-line utilities for turning meeting recordings and transcripts into summaries, classifications, and speaker segments.

## Overview

MeetSummarizer targets teams and individuals who want lightweight, scriptable meeting intelligence without a hosted service. Each module is a standalone CLI script that can also be imported as a library function. The stack centers on Hugging Face Transformers for summarization and sentiment, OpenAI Whisper for transcription, MoviePy for audio extraction, and pyAudioAnalysis for speaker diarization.

## Features

- Summarize long transcripts with adaptive length limits for short inputs.
- Format summary text into bullet lists (sentence splitting and existing list markers).
- Classify meeting type using keyword heuristics (client, interview, group discussion).
- Analyze tone and sentiment from transcript text.
- Extract audio from video files.
- Transcribe audio with configurable Whisper models.
- Diarize audio into per-speaker segment files.

## Tech stack

| Area | Libraries / tools |
| --- | --- |
| Language | Python 3.9+ |
| NLP | `transformers`, `nltk` (dependency chain) |
| Speech | `openai-whisper`, `SpeechRecognition` |
| Audio / video | `moviepy`, `pydub`, `librosa`, `pyAudioAnalysis` |
| Utilities | `numpy`, `scikit-learn` (used by audio analysis stack) |

FFmpeg is required at runtime for MoviePy and pydub when processing many video/audio formats.

## Prerequisites

- Python 3.9 or newer
- FFmpeg installed and available on your `PATH` (recommended for audio/video workflows)
- Sufficient disk space for downloaded model weights (Transformers and Whisper cache on first run)

## Getting started

Clone the repository and install dependencies:

```console
git clone https://github.com/vonmiller1/meetbots.git
cd meetbots
python -m pip install -r requirements.txt
```

No environment variables are required for the current CLI scripts. Model downloads use default Hugging Face and Whisper cache locations on your machine.

## Running locally

Run scripts from the repository root. Replace paths with your own files.

**Transcript workflow**

```console
python text_summarization.py transcript.txt --output summary.txt
python plan_of_action.py summary.txt --output plan_of_action.txt
python classify_meeting.py transcript.txt
python tone_analysis.py transcript.txt
python sentiment_analysis.py transcript.txt
```

**Audio workflow**

```console
python extract_audio.py meeting.mp4 meeting.wav
python audio_to_text.py meeting.wav --model base --output transcript.txt
python speaker_identification.py meeting.wav --speakers 2 --output-dir speaker_segments
```

Default output files: `summary.txt` (summarizer), `plan_of_action.txt` (action plan). Transcription prints to stdout unless `--output` is set.

## Testing

Unit tests live under `tests/` and use mocks so heavy ML dependencies are not loaded during test discovery:

```console
python -m unittest discover -s tests
```

This workflow does not execute tests automatically; run the command above when you want to verify behavior locally.

## Project structure

| Path | Purpose |
| --- | --- |
| `text_summarization.py` | Transcript summarization |
| `plan_of_action.py` | Bullet-list formatting from summaries |
| `classify_meeting.py` | Keyword-based meeting classification |
| `tone_analysis.py` | Keyword-based tone categorization |
| `sentiment_analysis.py` | Transformers sentiment pipeline |
| `extract_audio.py` | Video-to-audio extraction |
| `audio_to_text.py` | Whisper transcription |
| `speaker_identification.py` | Speaker diarization and segment export |
| `tests/test_helpers.py` | Unit tests for core helpers |
| `requirements.txt` | Python dependencies |

## Configuration

- **Whisper model:** `--model` on `audio_to_text.py` (default `base`).
- **Speaker count:** `--speakers` on `speaker_identification.py` (default `2`).
- **Output paths:** `--output`, `--output-dir` flags on respective scripts.

Generated artifacts such as `summary.txt`, `plan_of_action.txt`, and `speaker_segments/` are listed in `.gitignore`.

## Deployment

There is no bundled web server or Docker image in this repository. Deploy by installing dependencies on a machine with Python and FFmpeg, then invoking the scripts from cron, a workflow runner, or your own orchestration layer.

## Contributing

1. Fork the repository and create a feature branch from `main`.
2. Keep commits focused; prefer one logical change per commit.
3. Add or update tests in `tests/` when changing behavior.
4. Open a pull request with a short description of the change.

## License

No `LICENSE` file is present in this repository at this time. Contact the repository owner for usage terms if you need explicit licensing.
