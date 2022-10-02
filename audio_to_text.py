import whisper

def audio_to_text(audio_file_path, model_type="base"):
    # Load the Whisper model
    model = whisper.load_model(model_type)
    
    # Transcribe the audio file
    result = model.transcribe(audio_file_path)
    
    # Extract the transcribed text
    transcribed_text = result["text"]
    
    print("Transcription completed.")
    return transcribed_text

# Specify the path to the audio file
audio_file_path = "C:\\Users\\AFREEN\\Desktop\\MeetSummarizer\\Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\MileStone\\data\\output_audio.wav"

# Perform audio-to-text conversion
transcribed_text = audio_to_text(audio_file_path)

# Save the transcribed text to a file
output_text_file_path = "C:\\Users\\AFREEN\\Desktop\\MeetSummarizer\\Meeting-Summarizer-and-plan-of-action-generator-using-NLP_oct_2024\\MileStone\\data\\transcribed_text.txt"
with open(output_text_file_path, "w", encoding="utf-8") as file:
    file.write(transcribed_text)

print(f"Transcribed text saved to: {output_text_file_path}")
