from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

skills_db = [
    "python",
    "java",
    "c",
    "machine learning",
    "deep learning",
    "nlp",
    "sql",
    "data analysis",
    "tensorflow",
    "pandas",
    "flask",
    "streamlit",
    "cybersecurity",
    "ai",
    "html",
    "css",
    "javascript",
    "react",
    "mongodb",
    "mysql"
]



def get_similarity(resume, job_desc):
    texts = [resume, job_desc]

    cv = CountVectorizer(stop_words='english')
    matrix = cv.fit_transform(texts)

    score = cosine_similarity(matrix)[0][1]

    return round(score * 100, 2)



def extract_skills(text):
    found = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found.append(skill)

    return list(set(found))



def missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills) - set(resume_skills))



def generate_suggestions(score, missing):

    suggestions = []

    if score < 40:
        suggestions.append("Resume match is low. Add more job-related keywords.")

    if score >= 40 and score < 70:
        suggestions.append("Resume is average. Improve project descriptions and skills.")

    if score >= 70:
        suggestions.append("Strong resume match detected.")

    if len(missing) > 0:
        suggestions.append(f"Add missing skills: {', '.join(missing)}")

    return suggestions