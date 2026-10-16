# 📝 Meeting Summarizer & Plan of Action Generator (MeetSummarizer)

MeetSummarizer is an **NLP-powered application** that automatically generates **concise meeting summaries** and a **structured plan of action (POA)** from raw meeting transcripts or uploaded documents.  
It is designed to boost **team productivity** by reducing manual note-taking and ensuring **clear accountability** after meetings.  

---

## 📌 Features
- **Automatic Summarization** of meeting transcripts  
- **Action Item Extraction** with assigned responsibilities  
- **Keyword & Topic Detection** for quick insights  
- **Customizable Input** – supports text, PDF, or speech-to-text transcripts  
- **Plan of Action (POA) Generation** in a structured format  
- **Simple UI** for easy upload and analysis  

---

## 🏗️ System Architecture
1. **Input** – Upload meeting transcript (text/PDF/audio-to-text).  
2. **Preprocessing** – NLP-based cleaning and tokenization.  
3. **Summarization** – Transformer-based model generates concise summary.  
4. **Action Item Extraction** – NLP pipeline extracts tasks, deadlines, and responsibilities.  
5. **Output** – Summary + structured plan of action.  

---

## ⚙️ Tech Stack
- **Languages:** Python  
- **Frameworks:** Streamlit / Flask  
- **NLP Libraries:** NLTK, spaCy, Hugging Face Transformers  
- **Models:** BART / T5 / Pegasus (for summarization)  
- **Other Tools:** PyPDF2 (PDF parsing), SpeechRecognition (optional), OpenAI/Gemini APIs (optional)  

---

---

## 📌 Features

MeetSummarizer/
├── app.py                 # Streamlit/Flask app
├── requirements.txt       # Dependencies
├── src/
│   ├── summarizer.py      # NLP summarization module
│   ├── action_items.py    # Action item extraction module
│   └── utils.py           # Preprocessing utilities
├── data/
│   └── sample_transcript.txt
├── outputs/
│   └── summary.json
└── README.md


---

## 📊 Sample Output

**Meeting Summary:**
- Discussed upcoming product launch strategy.  
- Marketing team to finalize campaign timeline.  
- Engineering to resolve deployment pipeline issues.  

**Plan of Action (POA):**
- [ ] **John** → Draft marketing content by *Aug 20*  
- [ ] **Priya** → Fix CI/CD pipeline issue by *Aug 22*  
- [ ] **Alex** → Coordinate with sales team for client outreach  

---

## 🔮 Future Enhancements
- Integration with **Google Meet / Zoom APIs** for automatic transcript import  
- **Voice-to-Text conversion** for live meeting analysis  
- Export summaries and POA to **Slack, Trello, or Jira**  
- Support for **multi-lingual transcripts**  

---

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/USERNAME/MeetSummarizer.git
cd MeetSummarizer
```
---

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
---

### 3. Run the Application
```bash
streamlit run app.py
```
---

### 4. Upload Your Transcript
- Upload a `.txt` or `.pdf` file, or paste meeting text.  
- Click **Summarize** to generate results.  
---

