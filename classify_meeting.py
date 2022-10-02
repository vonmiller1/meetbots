def classify_meeting(text):
    """Classify the meeting type (e.g., client, interview, etc.) based on keywords."""
    if "client" in text or "project update" in text:
        meeting_type = "Client Meeting"
    elif "interview" in text:
        meeting_type = "Interview"
    elif "discussion" in text and "team" in text:
        meeting_type = "Group Discussion"
    else:
        meeting_type = "General Meeting"

    return meeting_type

if __name__ == "__main__":
    with open("data/text/transcription.txt", "r") as file:
        text = file.read()

    meeting_type = classify_meeting(text)
    print("Meeting Type: ", meeting_type)
