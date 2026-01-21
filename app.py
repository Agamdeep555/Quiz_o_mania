

import streamlit as st
from generate import generate_mcqs
from export import export_to_doc
from utils import extract_text_from_pdf

st.markdown("""<style>
/* ============================================
   QUIZ O MANIA - ADVANCED CSS STYLING
   ============================================ */

:root {
  --primary-color: #6C63FF;
  --primary-hover: #574FE0;
  --secondary-color: #FF6B9D;
  --success-color: #00D4FF;
  --error-color: #FF6B6B;
  --warning-color: #FFD93D;
  --dark-bg: #0F1117;
  --card-bg: #1C1F26;
  --border-color: #30363D;
  --text-primary: #E0E0E0;
  --text-secondary: #8B949E;
}

/* ============================================
   GLOBAL STYLES
   ============================================ */

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  background-color: var(--dark-bg);
  color: var(--text-primary);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
}

/* ============================================
   MAIN CONTAINER & LAYOUT
   ============================================ */

[data-testid="stAppViewContainer"] {
  background: linear-gradient(135deg, #0F1117 0%, #1a1f2e 100%);
}

[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0F1117 0%, #1C1F26 100%);
  border-right: 1px solid var(--border-color);
}

[data-testid="stMainBlockContainer"] {
  padding: 2rem;
  max-width: 1200px;
}

/* ============================================
   TYPOGRAPHY
   ============================================ */

h1, h2, h3, h4, h5, h6 {
  color: #FFFFFF;
  font-weight: 700;
  letter-spacing: -0.5px;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

h2 {
  font-size: 1.8rem;
  margin: 1.5rem 0 1rem 0;
}

h3 {
  font-size: 1.4rem;
  color: #E0E0E0;
}

p {
  color: var(--text-secondary);
  font-size: 1rem;
}

/* ============================================
   BUTTONS & INTERACTIONS
   ============================================ */

.stButton > button {
  background: linear-gradient(135deg, var(--primary-color) 0%, #5652D3 100%);
  color: white;
  border: none;
  border-radius: 10px;
  padding: 12px 24px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stButton > button:hover {
  background: linear-gradient(135deg, var(--primary-hover) 0%, #4A41C1 100%);
  box-shadow: 0 6px 20px rgba(108, 99, 255, 0.5);
  transform: translateY(-2px);
}

.stButton > button:active {
  transform: translateY(0);
  box-shadow: 0 2px 10px rgba(108, 99, 255, 0.3);
}

/* Secondary Button Style */
.stButton > button[kind="secondary"] {
  background: var(--card-bg);
  color: var(--primary-color);
  border: 2px solid var(--primary-color);
}

.stButton > button[kind="secondary"]:hover {
  background: var(--primary-color);
  color: white;
}

/* ============================================
   FORMS & INPUTS
   ============================================ */

.stForm {
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 2rem;
  background-color: var(--card-bg);
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.stRadio > label {
  color: var(--text-primary);
  font-weight: 500;
  padding: 12px;
  margin: 8px 0;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.stRadio > label:hover {
  background-color: rgba(108, 99, 255, 0.1);
  color: var(--primary-color);
}

.stRadio > div {
  gap: 12px;
}

.stSelectbox > div > div {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--text-primary);
}

input, select, textarea {
  background-color: var(--card-bg) !important;
  border: 1px solid var(--border-color) !important;
  color: var(--text-primary) !important;
  border-radius: 8px !important;
  padding: 10px 12px !important;
}

input:focus, select:focus, textarea:focus {
  border-color: var(--primary-color) !important;
  outline: none;
  box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.1) !important;
}

/* ============================================
   ALERTS & MESSAGES
   ============================================ */

.stSuccess {
  background-color: rgba(0, 212, 255, 0.1);
  border: 1px solid var(--success-color);
  border-radius: 10px;
  padding: 1rem;
  color: #00D4FF;
}

.stError {
  background-color: rgba(255, 107, 107, 0.1);
  border: 1px solid var(--error-color);
  border-radius: 10px;
  padding: 1rem;
  color: #FF6B6B;
}

.stWarning {
  background-color: rgba(255, 217, 61, 0.1);
  border: 1px solid var(--warning-color);
  border-radius: 10px;
  padding: 1rem;
  color: #FFD93D;
}

.stInfo {
  background-color: rgba(108, 99, 255, 0.1);
  border: 1px solid var(--primary-color);
  border-radius: 10px;
  padding: 1rem;
  color: var(--primary-color);
}

/* ============================================
   FILE UPLOADER
   ============================================ */

.stFileUploader {
  border-radius: 12px;
  border: 2px dashed var(--primary-color);
  padding: 2rem;
  text-align: center;
  transition: all 0.3s ease;
}

.stFileUploader:hover {
  border-color: var(--secondary-color);
  background-color: rgba(108, 99, 255, 0.05);
}

[data-testid="stFileUploadDropzone"] {
  border-radius: 12px;
  border: 2px dashed var(--primary-color);
  padding: 2rem;
}

/* ============================================
   SIDEBAR STYLING
   ============================================ */

.stSidebar .stMarkdown h2 {
  color: var(--primary-color);
  font-size: 1.5rem;
  margin-top: 0;
}

.stSidebar .stMarkdown h3 {
  color: #FFD93D;
  font-size: 1.1rem;
}

.stSidebar .stMarkdown p, 
.stSidebar .stMarkdown li {
  color: var(--text-secondary);
  font-size: 0.95rem;
}

.stSidebar hr {
  border: none;
  border-top: 1px solid var(--border-color);
  margin: 1.5rem 0;
}

/* ============================================
   CARDS & CONTAINERS
   ============================================ */

[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
  margin: 1rem 0;
  transition: all 0.3s ease;
}

[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"]:hover {
  border-color: var(--primary-color);
  box-shadow: 0 8px 24px rgba(108, 99, 255, 0.15);
}

/* ============================================
   QUESTION STYLING
   ============================================ */

.stSubheader {
  color: var(--primary-color);
  font-weight: 700;
  font-size: 1.3rem;
  padding: 1rem;
  background: linear-gradient(90deg, rgba(108, 99, 255, 0.1) 0%, transparent 100%);
  border-left: 4px solid var(--primary-color);
  border-radius: 6px;
  margin: 1.5rem 0 1rem 0;
}

/* ============================================
   SCROLLBAR
   ============================================ */

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: var(--dark-bg);
}

::-webkit-scrollbar-thumb {
  background: var(--primary-color);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--primary-hover);
}

/* ============================================
   RESPONSIVE DESIGN
   ============================================ */

@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  .stForm {
    padding: 1.5rem;
  }

  [data-testid="stMainBlockContainer"] {
    padding: 1rem;
  }

  .stButton > button {
    width: 100%;
    padding: 14px 20px;
  }
}

/* ============================================
   ANIMATIONS
   ============================================ */

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

[data-testid="stVerticalBlock"] {
  animation: fadeIn 0.5s ease-out;
}

.stSidebar {
  animation: slideInLeft 0.5s ease-out;
}

/* ============================================
   SPINNER & LOADING
   ============================================ */

[data-testid="stSpinner"] {
  color: var(--primary-color);
}
</style>""", unsafe_allow_html=True)


def display_mcq(mcqs):
    st.title("Multiple Choice Questions")
    

    # Ensure correct initialization of answer tracking
    if 'user_answers' not in st.session_state or len(st.session_state.user_answers) != len(mcqs):
        st.session_state.user_answers = [None] * len(mcqs)

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if st.button("Reset Choices"):
        for idx in range(len(mcqs)):
            st.session_state.pop(f"q_{idx}", None)
        st.session_state.user_answers = [None] * len(mcqs)
        st.session_state.submitted = False
        st.rerun()

    # 🔧 Form with submit button inside
    with st.form("mcq_form"):
        for idx, mcq in enumerate(mcqs):
            st.subheader(mcq['question'])
            options = mcq['choices']
            st.session_state.user_answers[idx] = st.radio(
                f"Select your answer for Question {idx+1}:",
                options,
                key=f"q_{idx}"
            )

        # ✅ Submit button placed inside the form block
        submitted = st.form_submit_button("Submit All Answers")
        if submitted:
            st.session_state.submitted = True

    # 🧠 Evaluation
    if st.session_state.submitted:
        correct = 0
        for idx, mcq in enumerate(mcqs):
            user_answer = st.session_state.user_answers[idx]
            correct_answer = mcq['answer']

            if user_answer == correct_answer:
                st.success(f"Question {idx+1}: Correct! The answer is {correct_answer}")
                correct += 1
            else:
                st.error(f"Question {idx+1}: Incorrect. The correct answer is {correct_answer}")

            # Show explanation if present
            if "explanation" in mcq:
                st.markdown(f"**🧠 Explanation:** {mcq['explanation']}")

        st.info(f"🎯 Final Score: {correct}/{len(mcqs)}")

    # 📄 Export option
    if st.button("Export to DOC"):
        doc_buffer = export_to_doc(mcqs)
        st.download_button(
            label="Download DOC",
            data=doc_buffer,
            file_name="mcqs.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )


def main():
    # 🌈 Page Config
    st.set_page_config(
        page_title="Quiz O Mania",
        page_icon="🧠",
        layout="wide"
    )

    # 🎯 Sidebar UI
    st.sidebar.markdown("## 🎯 Quiz-O-Mania")
    st.sidebar.caption("AI-powered MCQ Generator from PDFs")

    uploaded_file = st.sidebar.file_uploader(
        "📄 Upload a PDF",
        type="pdf"
    )

    difficulty = st.sidebar.selectbox(
        "🎚 Select Difficulty Level",
        ["Easy", "Medium", "Hard"]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("💡 **How it works**")
    st.sidebar.markdown("""
    1. Upload a PDF  
    2. Choose difficulty  
    3. Attempt MCQs  
    4. Check score  
    5. Export questions  
    """)

    # 🖥 Main Area
    st.markdown("# 🎓 Quiz O Mania")
    st.markdown("### Turn PDFs into interactive quizzes instantly")

    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)

        if st.sidebar.button("🚀 Generate New Questions"):
            st.session_state.pop('mcqs', None)
            st.session_state.user_answers = []
            st.session_state.submitted = False

            for idx in range(10):
                st.session_state.pop(f"q_{idx}", None)

            st.rerun()

        if 'mcqs' not in st.session_state:
            with st.spinner("🤖 Generating intelligent MCQs..."):
                st.session_state.mcqs = generate_mcqs(pdf_text, difficulty)

        if st.session_state.mcqs:
            st.success(f"✅ MCQs generated successfully — **{difficulty} Level**")
            display_mcq(st.session_state.mcqs)
        else:
            st.error("❌ Failed to generate MCQs. Try another PDF.")

    else:
        st.info("📄 Upload a PDF from the sidebar to begin.")


if __name__ == "__main__":
    main()

