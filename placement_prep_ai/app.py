"""Placement Preparation with AI Resume Analyzer - Streamlit app.

Run with:  streamlit run app.py
"""
import pandas as pd
import streamlit as st

from analyzer import analyze, extract_text, learning_plan, text_report
from skills_db import (APTITUDE_QUIZ, HR_QUESTIONS, PREP_TOPICS, ROLE_QUESTIONS,
                       ROLES, SKILL_QUESTIONS)

st.set_page_config(page_title="PlacePrep AI", page_icon="🎯", layout="wide")


def read_sample(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


# ------------------------------------------------------------------ sidebar
st.sidebar.title("🎯 PlacePrep AI")
st.sidebar.caption("Placement preparation with AI resume analyzer")
role = st.sidebar.selectbox("Target role", list(ROLES.keys()))
jd_text = st.sidebar.text_area(
    "Paste a job description (optional)", height=180,
    placeholder="If you paste a JD, your resume is compared against it instead of the generic role.")
if st.sidebar.checkbox("Use sample job description"):
    jd_text = read_sample("sample_job_description.txt")
    st.sidebar.info("Sample JD loaded.")

st.title("🎯 Placement Preparation & AI Resume Analyzer")
st.write("Upload your resume, get an ATS-style score, skill-gap report, interview questions, "
         "a quick aptitude quiz and a preparation tracker - all in one place.")

# ------------------------------------------------------------ resume input
col_a, col_b = st.columns([2, 1])
with col_a:
    uploaded = st.file_uploader("Upload resume (PDF / DOCX / TXT)", type=["pdf", "docx", "txt"])
with col_b:
    use_sample = st.checkbox("Use sample resume (for demo)")

resume_text = ""
if uploaded is not None:
    resume_text = extract_text(uploaded.name, uploaded.getvalue())
elif use_sample:
    resume_text = read_sample("sample_resume.txt")

if not resume_text.strip():
    st.info("👆 Upload a resume or tick **Use sample resume** to begin.")
    resume_result = None
else:
    resume_result = analyze(resume_text, role, jd_text)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📄 Resume Analyzer", "🧩 Skill Gap & Plan", "🎤 Interview Prep", "📝 Aptitude Quiz", "📈 Prep Tracker"])

# ------------------------------------------------------------------- tab 1
with tab1:
    if resume_result is None:
        st.write("Your analysis will appear here.")
    else:
        r = resume_result
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Overall Score", f"{r['overall']}/100")
        c2.metric("Skill Match", f"{r['parts']['Skill Match']}%")
        c3.metric("Role/JD Similarity", f"{r['parts']['JD / Role Similarity']}%")
        c4.metric("Word Count", r["words"])
        st.progress(min(int(r["overall"]), 100) / 100)
        st.subheader(r["grade"])
        st.caption(f"Skills compared against: {r['source']}")

        left, right = st.columns(2)
        with left:
            st.markdown("#### Score breakdown")
            df = pd.DataFrame({"Category": list(r["parts"].keys()),
                               "Score": list(r["parts"].values())}).set_index("Category")
            st.bar_chart(df)
        with right:
            st.markdown("#### Resume sections detected")
            sec = pd.DataFrame({"Section": [s.title() for s in r["sections"]],
                                "Present": ["✅" if v else "❌" for v in r["sections"].values()]})
            st.dataframe(sec, hide_index=True, use_container_width=True)
            contact_txt = "  ".join(f"{'✅' if v else '❌'} {k.title()}" for k, v in r["contact"].items())
            st.write("**Contact & links:** " + contact_txt)
            st.write(f"**Action verbs:** {r['verbs']}   |   **Quantified points:** {r['quantified']}")

        st.markdown("#### 💡 Improvement suggestions")
        for tip in r["suggestions"]:
            st.write("• " + tip)

        st.download_button("⬇️ Download report (.txt)", text_report(role, r), file_name="resume_report.txt")
        with st.expander("View extracted resume text"):
            st.text(resume_text)

# ------------------------------------------------------------------- tab 2
with tab2:
    if resume_result is None:
        st.write("Upload a resume to see your skill gap.")
    else:
        r = resume_result
        m1, m2, m3 = st.columns(3)
        m1.metric("Matched skills", len(r["matched"]))
        m2.metric("Missing skills", len(r["missing"]))
        m3.metric("Extra skills", len(r["extra"]))

        st.success("✅ Matched: " + (", ".join(r["matched"]) or "none"))
        st.error("❌ Missing: " + (", ".join(r["missing"]) or "none - great!"))
        st.info("➕ Other skills found: " + (", ".join(r["extra"]) or "none"))

        st.markdown("#### Skills found by category")
        cat_df = (pd.Series(r["resume_skills"]).value_counts().rename_axis("Category")
                  .reset_index(name="Count").set_index("Category")) if r["resume_skills"] else None
        if cat_df is not None:
            st.bar_chart(cat_df)

        st.markdown("#### 📚 Personal learning plan")
        plan = learning_plan(r["missing"])
        if plan:
            st.dataframe(pd.DataFrame(plan, columns=["Skill to learn", "How to learn it"]),
                         hide_index=True, use_container_width=True)
        else:
            st.write("No gaps found. Focus on projects and mock interviews!")

# ------------------------------------------------------------------- tab 3
with tab3:
    st.markdown(f"#### Technical questions for **{role}**")
    for i, q in enumerate(ROLE_QUESTIONS[role], 1):
        with st.expander(f"Q{i}. {q}"):
            st.write("Tip: structure your answer as **Definition → Example → Real-world use**. "
                     "Practise saying it aloud in under 90 seconds.")

    if resume_result is not None:
        qs = [SKILL_QUESTIONS[s] for s in resume_result["resume_skills"] if s in SKILL_QUESTIONS]
        if qs:
            st.markdown("#### Questions based on skills in YOUR resume")
            st.caption("Interviewers pick questions from what you wrote - be ready for every skill listed.")
            for q in qs:
                st.write("• " + q)

    st.markdown("#### HR round")
    for q in HR_QUESTIONS:
        st.write("• " + q)

# ------------------------------------------------------------------- tab 4
with tab4:
    st.markdown("#### Quick aptitude + CS quiz")
    with st.form("quiz"):
        answers = []
        for i, item in enumerate(APTITUDE_QUIZ):
            answers.append(st.radio(f"Q{i + 1}. {item['q']}", item["options"], index=None, key=f"quiz{i}"))
        submitted = st.form_submit_button("Submit")
    if submitted:
        score = sum(1 for a, item in zip(answers, APTITUDE_QUIZ) if a == item["answer"])
        st.subheader(f"Score: {score}/{len(APTITUDE_QUIZ)}")
        for i, (a, item) in enumerate(zip(answers, APTITUDE_QUIZ), 1):
            ok = a == item["answer"]
            st.write(f"{'✅' if ok else '❌'} Q{i}: correct answer **{item['answer']}** - {item['why']}")

# ------------------------------------------------------------------- tab 5
with tab5:
    st.markdown("#### Placement preparation tracker")
    st.caption("Update the status and hours; progress is calculated automatically.")
    if "tracker" not in st.session_state:
        st.session_state.tracker = pd.DataFrame({
            "Topic": PREP_TOPICS,
            "Status": ["Not started"] * len(PREP_TOPICS),
            "Hours spent": [0.0] * len(PREP_TOPICS),
        })
    edited = st.data_editor(
        st.session_state.tracker, hide_index=True, use_container_width=True, num_rows="fixed",
        column_config={
            "Status": st.column_config.SelectboxColumn(options=["Not started", "In progress", "Done"]),
            "Hours spent": st.column_config.NumberColumn(min_value=0.0, step=0.5),
            "Topic": st.column_config.TextColumn(disabled=True),
        })
    st.session_state.tracker = edited
    done = (edited["Status"] == "Done").sum()
    pct = done / len(edited)
    st.progress(pct)
    k1, k2, k3 = st.columns(3)
    k1.metric("Topics completed", f"{done}/{len(edited)}")
    k2.metric("Readiness", f"{pct * 100:.0f}%")
    k3.metric("Total hours", f"{edited['Hours spent'].sum():.1f}")
    st.bar_chart(edited["Status"].value_counts())
