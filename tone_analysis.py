def analyze_tone(text):
    """Analyze the tone of the given text.
    
    The tone can be categorized based on pace, language style, etc.
    This is a simplified approach and can be extended using NLP models.
    """
    # Example analysis: Checking for specific keywords
    if "urgent" in text or "immediately" in text:
        tone = "Fast-paced and urgent"
    elif "discussion" in text or "meeting" in text:
        tone = "Professional"
    else:
        tone = "Casual"

    return tone

if __name__ == "__main__":
    with open("data/text/transcription.txt", "r") as file:
        text = file.read()

    tone = analyze_tone(text)
    print("Tone Analysis: ", tone)
