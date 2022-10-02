import os
import wave
from pyAudioAnalysis import audioSegmentation as aS
from pydub import AudioSegment

def perform_speaker_diarization(audio_file_path, n_speakers=2, output_dir="speaker_segments"):
    """
    Perform speaker diarization using pyAudioAnalysis and save speaker segments as audio files.
    
    Parameters:
    - audio_file_path: Path to the input audio file.
    - n_speakers: Number of expected speakers in the audio.
    - output_dir: Directory to save the speaker-segmented audio files.
    
    Returns:
    - A dictionary with speaker labels as keys and their time segments (start, end) as values.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Perform speaker diarization
    flags, classes, _ = aS.speaker_diarization(audio_file_path, n_speakers=n_speakers, plot_res=False)

    # Initialize the dictionary to store the segments
    speaker_segments = {}
    num_speakers = len(set(classes))

    for i in range(num_speakers):
        speaker_segments[f"speaker_{i + 1}"] = []

    # Read the input audio file with pydub for segment extraction
    audio = AudioSegment.from_wav(audio_file_path)
    frame_rate = audio.frame_rate
    total_duration = len(audio) / 1000  # Convert from milliseconds to seconds

    # Segment the audio into time windows (timestamps)
    segment_duration = total_duration / len(flags)
    
    # Extract and save speaker segments
    for idx, speaker_label in enumerate(classes):
        timestamp_start = int(idx * segment_duration * 1000)  # Convert to milliseconds
        timestamp_end = int((idx + 1) * segment_duration * 1000)  # Convert to milliseconds
        speaker_segment = audio[timestamp_start:timestamp_end]
        
        speaker_file_name = os.path.join(output_dir, f"speaker_{speaker_label + 1}_{timestamp_start}_{timestamp_end}.wav")
        speaker_segment.export(speaker_file_name, format="wav")
        speaker_segments[f"speaker_{speaker_label + 1}"].append((timestamp_start / 1000, timestamp_end / 1000))  # Store in seconds

    print("Speaker identification and segment extraction completed.")
    return speaker_segments

# Path to the audio file and output directory
audio_file_path = "C:\\Users\\AFREEN\\Desktop\\MeetSummarizer\\Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\MileStone\\data\\output_audio.wav"
output_dir = "C:\\Users\\AFREEN\\Desktop\\MeetSummarizer\\Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\MileStone\\data\\speaker_segments"

# Identify speakers and save segments as separate audio files
speaker_segments = perform_speaker_diarization(audio_file_path, n_speakers=2, output_dir=output_dir)

# Print speaker segments
for speaker, timestamps in speaker_segments.items():
    print(f"{speaker}: {timestamps}")
