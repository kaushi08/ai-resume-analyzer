import streamlit as st
import pandas as pd

from parser import extract_text_from_pdf
from parser import extract_text_from_docx

from analyzer import get_similarity
from analyzer import extract_skills
from analyzer import missing_skills
from analyzer import generate_suggestions

from database import save_result
from database import get_results

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 Advanced AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:

    file_type = uploaded_file.name.split(".")[-1]

    if file_type == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)

    else:
        resume_text = extract_text_from_docx(uploaded_file)

    score = get_similarity(resume_text, job_desc)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_desc)

    missing = missing_skills(resume_skills, jd_skills)

    suggestions = generate_suggestions(score, missing)

    save_result(uploaded_file.name, score)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 ATS Match Score")
        st.progress(int(score))
        st.write(f"### {score}%")

    with col2:
        st.subheader("📌 Resume Skills")
        st.write(resume_skills)

    st.subheader("❌ Missing Skills")
    st.write(missing)

    st.subheader("💡 Suggestions")

    for suggestion in suggestions:
        st.write("-", suggestion)

    chart_data = pd.DataFrame({
        "Category": ["Matched Skills", "Missing Skills"],
        "Count": [len(resume_skills), len(missing)]
    })

    st.subheader("📈 Skill Analysis")
    st.bar_chart(chart_data.set_index("Category"))

st.subheader("📂 Previous Analyses")

results = get_results()

if results:
    df = pd.DataFrame(results, columns=["ID", "Filename", "Score"])
    st.dataframe(df)