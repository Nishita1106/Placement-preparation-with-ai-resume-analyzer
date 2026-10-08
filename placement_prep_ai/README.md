# Placement Preparation with AI Resume Analyzer

A Python project that helps students prepare for campus placements. It analyses a resume (PDF / DOCX / TXT),
scores it like an ATS (Applicant Tracking System), finds skill gaps for a chosen job role, and offers interview
questions, an aptitude quiz and a preparation tracker.

## Features
1. **Resume Analyzer** - overall score out of 100 with a breakdown (skill match, JD similarity, sections,
   contact links, action verbs + quantified impact, length) and improvement suggestions.
2. **Skill Gap & Learning Plan** - matched / missing / extra skills and a plan for each missing skill.
3. **Job Description Matching** - paste any JD; the resume is compared against it using TF-IDF + cosine similarity.
4. **Interview Prep** - role specific technical questions, questions generated from skills in *your* resume, HR questions.
5. **Aptitude + CS Quiz** - instant scoring with explanations.
6. **Prep Tracker** - editable table with progress and hours, built with pandas.
7. **Downloadable report** (.txt).

## Tech stack
Python, Streamlit, Pandas, NumPy, scikit-learn (TF-IDF, cosine similarity), pypdf, python-docx, regex.

## How the "AI" works
- **Skill extraction:** a skills knowledge base (about 90 skills with aliases) is matched with regular expressions.
- **Similarity:** the resume and the job description are converted to TF-IDF vectors (unigrams + bigrams) and
  compared with cosine similarity.
- **Scoring:** weighted average (NumPy) of six components: Skill Match 40, JD/Role Similarity 20, Sections 15,
  Impact 10, Length 10, Contact 5.
- **Suggestions:** rule based recommendations generated from what is missing.

## Run it
```bash
pip install -r requirements.txt
streamlit run app.py
```
The app opens at http://localhost:8501. Tick **Use sample resume** for an instant demo, or upload your own resume.

## Project structure
```
app.py                       Streamlit user interface
analyzer.py                  NLP, ATS checks and scoring engine
skills_db.py                 Skills, roles, question banks, learning hints
sample_resume.txt            Demo resume
sample_job_description.txt   Demo job description
requirements.txt             Dependencies
```

## Limitations and future scope
- Rule based + classical NLP (no external API needed, works offline).
- Future: LLM-based feedback, resume templates, company-specific question banks, database to save user progress.
