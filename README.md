# MeetSummarizer

MeetSummarizer is a collection of Python command-line tools for working with
meeting transcripts and recordings. Use the tools individually to summarize
transcripts, generate a bullet list from a summary, classify meeting content,
analyze sentiment and tone, or extract and process audio.

## Capabilities

- **Transcript tools:** summarize text, create a simple bullet list from a
  summary, classify meeting type using keywords, and analyze tone and sentiment.
- **Audio tools:** extract an audio track from video, transcribe audio with
  Whisper, and diarize recordings into speaker segments.
- **Python helpers:** each utility exposes a function that can be imported
  without starting command-line processing.

The action-plan utility formats sentences or existing list entries as bullets;
it does not identify or infer tasks from the text.

## Requirements and setup

- Python 3.9 or newer
- Install the Python dependencies:

  ```console
  python -m pip install -r requirements.txt
  ```

- Audio and video processing may also require FFmpeg and platform-supported
  codecs. Install these separately using your operating system's package
  manager.

The summarization and sentiment tools use Transformers, and transcription uses
Whisper. Their models may be downloaded the first time they run.

## Command-line usage

Run a script from the repository root and pass the input file path:

```console
python text_summarization.py transcript.txt --output summary.txt
python plan_of_action.py summary.txt --output plan_of_action.txt
python classify_meeting.py transcript.txt
python tone_analysis.py transcript.txt
python sentiment_analysis.py transcript.txt
```

Audio workflows:

```console
python extract_audio.py meeting.mp4 meeting.wav
python audio_to_text.py meeting.wav --model base --output transcript.txt
python speaker_identification.py meeting.wav --speakers 2 --output-dir speaker_segments
```

`plan_of_action.py` writes to `plan_of_action.txt` by default. The summarizer
writes to `summary.txt` by default. Transcription prints to standard output
unless `--output` is supplied.

## Project layout

| File | Purpose |
| --- | --- |
| `text_summarization.py` | Summarize a transcript |
| `plan_of_action.py` | Format summary text as a bullet list |
| `classify_meeting.py` | Classify meeting type with keyword rules |
| `tone_analysis.py` | Categorize tone with keyword rules |
| `sentiment_analysis.py` | Analyze sentiment with a Transformers pipeline |
| `extract_audio.py` | Extract audio from video |
| `audio_to_text.py` | Transcribe audio with Whisper |
| `speaker_identification.py` | Detect speaker segments and save audio clips |

## Tests

Run the standard-library unit tests with:

```console
python -m unittest discover -s tests
```
