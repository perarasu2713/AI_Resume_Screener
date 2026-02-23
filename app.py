import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
from pdf_parser import extract_text_from_pdf
from matcher import calculate_similarity

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Intelligence",
    page_icon="🧠",
    layout="wide"
)

# ---------------- ULTRA GOD CSS ----------------
st.markdown("""
<style>

/* ====== ANIMATED AURORA BACKGROUND ====== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1f1c2c);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ===== FADE IN ===== */
.main {
    animation: fadeIn 1.2s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px);}
    to { opacity: 1; transform: translateY(0);}
}

/* ===== GLASS CARDS ===== */
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 0 30px rgba(0,255,255,0.2);
    transition: 0.4s ease;
    margin-bottom: 25px;
}

.glass:hover {
    transform: scale(1.04);
    box-shadow: 0 0 60px rgba(0,255,255,0.6);
}

/* ===== ANIMATED TITLE ===== */
.title {
    font-size: 60px;
    text-align: center;
    font-weight: bold;
    background: linear-gradient(90deg,#00f5a0,#00d9f5,#ff00ff,#00f5a0);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 8s ease infinite;
}

@keyframes glow {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ===== METRIC CARDS ===== */
.metric {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    transition: 0.4s;
}

.metric:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 40px rgba(255,0,255,0.5);
}

/* ===== BUTTON ===== */
.stButton>button {
    background: linear-gradient(90deg,#00f5a0,#00d9f5);
    color: black;
    font-weight: bold;
    border-radius: 40px;
    padding: 10px 30px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 20px #00f5a0;
}

/* ===== SMOOTH SCROLL ===== */
html {
    scroll-behavior: smooth;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.markdown('<div class="title">🔐 HR Secure Portal</div>', unsafe_allow_html=True)
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "admin123":
            st.session_state.logged_in = True
            st.success("Access Granted 🚀")
        else:
            st.error("Access Denied ❌")

if not st.session_state.logged_in:
    login()
    st.stop()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🧠 AI Control Panel")
page = st.sidebar.radio("Navigate", ["Dashboard", "Resume Screening"])

logo = st.sidebar.file_uploader("Upload Company Logo", type=["png","jpg","jpeg"])
if logo:
    st.sidebar.image(logo, use_column_width=True)

# ---------------- SKILLS ----------------
SKILLS_DB = [
    "python","java","c++","html","css","javascript",
    "react","node","flask","django","sql","mongodb",
    "machine learning","deep learning","tensorflow",
    "pytorch","git","rest api"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS_DB if skill in text]

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.markdown('<div class="title">🧠 AI Resume Intelligence</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass">
    <h3>Futuristic Applicant Tracking System</h3>
    <p>Powered by Transformer-based Semantic Matching Engine.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SCREENING ----------------
if page == "Resume Screening":

    st.markdown('<div class="title">🚀 Resume Screening Engine</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)
    with col2:
        job_desc = st.text_area("Enter Job Description", height=200)

    if uploaded_files and job_desc:

        # ---- AI LOADING EFFECT ----
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
        progress.empty()

        results = []
        all_skills = []

        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            score = calculate_similarity(resume_text, job_desc)
            skills = extract_skills(resume_text)

            all_skills.extend(skills)

            results.append({
                "Candidate Name": file.name,
                "Match Score (%)": score,
                "Skills Found": ", ".join(skills)
            })

        df = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)

        # ---- ANIMATED METRICS ----
        def animate(label, value):
            placeholder = st.empty()
            for i in range(int(value)+1):
                placeholder.markdown(f"""
                <div class="metric">
                <h2>{i}%</h2>
                <p>{label}</p>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.02)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="metric">
            <h2>{len(df)}</h2>
            <p>Total Candidates</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            animate("Top Score", df.iloc[0]["Match Score (%)"])

        with c3:
            animate("Average Score", round(df["Match Score (%)"].mean(),2))

        # ---- TABLE ----
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---- PIE CHART ----
        skill_count = pd.Series(all_skills).value_counts()
        if not skill_count.empty:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            plt.figure()
            plt.pie(skill_count, labels=skill_count.index, autopct="%1.1f%%")
            st.pyplot(plt)
            st.markdown('</div>', unsafe_allow_html=True)

        # ---- BAR CHART ----
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        plt.figure()
        plt.bar(df["Candidate Name"], df["Match Score (%)"])
        plt.xticks(rotation=45)
        st.pyplot(plt)
        st.markdown('</div>', unsafe_allow_html=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Report", csv, "resume_report.csv", "text/csv")
