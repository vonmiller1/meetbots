# MeetSummarizer

MeetSummarizer contains command-line utilities for analyzing meeting transcripts
and processing meeting audio. It can summarize text, create a simple action-item
list, classify meeting type and tone, analyze sentiment, extract audio from
video, transcribe audio, and diarize speakers.

## Requirements

- Python 3.9 or newer
- Install Python packages with `python -m pip install -r requirements.txt`
- Audio utilities may require platform dependencies such as FFmpeg and the
  codecs used by MoviePy, Whisper, and pydub.

## Usage

Each script accepts paths as command-line arguments and can be imported without
starting processing:

```console
python text_summarization.py transcript.txt --output summary.txt
python plan_of_action.py summary.txt --output plan_of_action.txt
python classify_meeting.py transcript.txt
python tone_analysis.py transcript.txt
python sentiment_analysis.py transcript.txt
python extract_audio.py meeting.mp4 meeting.wav
python audio_to_text.py meeting.wav --model base --output transcript.txt
python speaker_identification.py meeting.wav --speakers 2 --output-dir speaker_segments
```

The transformer-based summarization and sentiment tools may download a model on
their first run. Audio utilities may also need system audio codecs.

## Tests

Run the standard-library unit tests with:

```console
python -m unittest discover -s tests
```
