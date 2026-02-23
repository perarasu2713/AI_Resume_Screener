# 🧠 AI Resume Intelligence System

An advanced AI-powered Resume Screening & Ranking Web Application built using Streamlit and Transformer-based Semantic Matching.

This project simulates a real-world Applicant Tracking System (ATS) used by companies to shortlist candidates intelligently.

---

## 🚀 Live Demo

👉 [Add your Streamlit deployment link here]

---

## 📌 Features

✅ Multi Resume Upload (PDF)  
✅ Transformer-Based Semantic Matching (BERT)  
✅ Resume Ranking Table (Top Candidates First)  
✅ Skill Extraction & Highlighting  
✅ Animated Score Counter  
✅ Pie Chart – Skill Distribution  
✅ Bar Graph – Candidate Comparison  
✅ Downloadable CSV Report  
✅ Company Logo Upload  
✅ Secure Login System  
✅ Glassmorphism UI with Smooth Animations  
✅ Dark Themed SaaS-Style Design  

---

## 🛠 Tech Stack

- Python
- Streamlit
- Sentence Transformers (all-MiniLM-L6-v2)
- PyTorch
- Scikit-learn
- Pandas
- Matplotlib
- PyPDF2
- NLTK

---

## 🧠 How It Works

1. Upload multiple resumes in PDF format.
2. Enter Job Description.
3. The system:
   - Extracts resume text
   - Converts text into embeddings using Transformer model
   - Calculates cosine similarity
   - Ranks candidates based on match score
4. Displays:
   - Ranked candidates
   - Skills detected
   - Visual analytics
5. Allows report download as CSV.
