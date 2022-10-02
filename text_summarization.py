from transformers import pipeline

def summarize_text(text):
    """Summarize the given text using a transformer-based summarizer."""
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    with open("data/text/transcription.txt", "r") as file:
        text = file.read()

    summary = summarize_text(text)
    print("Summary: ", summary)

    # Save the summary to a text file
    with open("data/text/summary.txt", "w") as f:
        f.write(summary)
