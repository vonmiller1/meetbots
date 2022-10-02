from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_file_path, output_audio_path):
    try:
        # Load the video file
        video = VideoFileClip(video_file_path)
        
        # Extract the audio
        audio = video.audio
        
        # Save the extracted audio to the specified path
        audio.write_audiofile(output_audio_path)
        print(f"Audio extracted and saved to: {output_audio_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the video file and the output audio file
video_file_path = "C:\\Users\\AFREEN\\Desktop\\MeetSummarizer\\Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\MileStone\\data\\input_zoom.mp4"
output_audio_path = "C:\\Users\\AFREEN\\Desktop\\MeetSummarizer\\Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\MileStone\\data\\output_audio.wav"

# Extract audio from the video
extract_audio_from_video(video_file_path, output_audio_path)
