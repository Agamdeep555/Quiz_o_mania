import streamlit as st
from generate import generate_mcqs
from export import export_to_doc
from utils import extract_text_from_pdf

# ============================================
# ADVANCED CSS STYLING FOR QUIZ O MANIA
# ============================================

st.markdown("""
<style>
:root {
  --primary-color: #6C63FF;
  --primary-hover: #574FE0;
  --secondary-color: #FF6B9D;
  --success-color: #00D4FF;
  --error-color: #FF6B6B;
  --warning-color: #FFD93D;
  --info-color: #6C63FF;
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

html, body, [data-testid="stAppViewContainer"] {
  background: linear-gradient(135deg, #0F1117 0%, #1a1f2e 100%) !important;
  color: var(--text-primary);
}

/* ============================================
   SIDEBAR STYLING
   ============================================ */

[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0F1117 0%, #1C1F26 100%) !important;
  border-right: 1px solid var(--border-color);
}

[data-testid="stSidebarContent"] {
  background: transparent;
}

.stSidebar .stMarkdown h2 {
  color: var(--primary-color) !important;
  font-size: 1.5rem !important;
  margin-top: 0 !important;
  font-weight: 700 !important;
}

.stSidebar .stMarkdown h3,
.stSidebar .stMarkdown strong {
  color: var(--warning-color) !important;
  font-weight: 600 !important;
}

.stSidebar .stMarkdown p,
.stSidebar .stMarkdown li {
  color: var(--text-secondary) !important;
  font-size: 0.95rem !important;
}

.stSidebar .stCaption {
  color: var(--text-secondary) !important;
  font-size: 0.85rem !important;
}

.stSidebar hr {
  border: none !important;
  border-top: 1px solid var(--border-color) !important;
  margin: 1.5rem 0 !important;
}

/* ============================================
   FILE UPLOADER STYLING
   ============================================ */

[data-testid="stFileUploadDropzone"] {
  border-radius: 12px !important;
  border: 2px dashed var(--primary-color) !important;
  padding: 2rem !important;
  background: rgba(108, 99, 255, 0.05) !important;
  transition: all 0.3s ease !important;
}

[data-testid="stFileUploadDropzone"]:hover {
  border-color: var(--secondary-color) !important;
  background: rgba(108, 99, 255, 0.1) !important;
  box-shadow: 0 4px 12px rgba(108, 99, 255, 0.2) !important;
}

.stFileUploader label {
  color: var(--text-primary) !important;
}

/* ============================================
   SELECTBOX & DROPDOWN STYLING
   ============================================ */

[data-testid="stSelectbox"] {
  margin: 1rem 0 !important;
}

.stSelectbox > div > div {
  background-color: var(--card-bg) !important;
  border: 1px solid var(--border-color) !important;
  border-radius: 8px !important;
  color: var(--text-primary) !important;
  transition: all 0.3s ease !important;
}

.stSelectbox > div > div:hover {
  border-color: var(--primary-color) !important;
  box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.1) !important;
}

/* ============================================
   BUTTON STYLING
   ============================================ */

.stButton > button {
  background: linear-gradient(135deg, var(--primary-color) 0%, #5652D3 100%) !important;
  color: white !important;
  border: none !important;
  border-radius: 10px !important;
  padding: 12px 24px !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  cursor: pointer !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
  box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  width: 100% !important;
}

.stButton > button:hover {
  background: linear-gradient(135deg, var(--primary-hover) 0%, #4A41C1 100%) !important;
  box-shadow: 0 6px 20px rgba(108, 99, 255, 0.5) !important;
  transform: translateY(-2px) !important;
}

.stButton > button:active {
  transform: translateY(0) !important;
  box-shadow: 0 2px 10px rgba(108, 99, 255, 0.3) !important;
}

/* ============================================
   FORM STYLING
   ============================================ */

.stForm {
  border: 1px solid var(--border-color) !important;
  border-radius: 12px !important;
  padding: 2rem !important;
  background-color: var(--card-bg) !important;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
  animation: slideUp 0.5s ease-out !important;
}

/* ============================================
   RADIO BUTTON STYLING
   ============================================ */

.stRadio > label {
  color: var(--text-primary) !important;
  font-weight: 500 !important;
  padding: 12px 14px !important;
  margin: 8px 0 !important;
  border-radius: 8px !important;
  border: 1px solid transparent !important;
  transition: all 0.2s ease !important;
  cursor: pointer !important;
}

.stRadio > label:hover {
  background-color: rgba(108, 99, 255, 0.1) !important;
  color: var(--primary-color) !important;
  border-color: var(--primary-color) !important;
}

.stRadio > div {
  gap: 12px !important;
}

/* ============================================
   HEADINGS & TYPOGRAPHY
   ============================================ */

h1, h2, h3, h4, h5, h6 {
  color: #FFFFFF !important;
  font-weight: 700 !important;
  letter-spacing: -0.5px !important;
}

h1 {
  font-size: 2.5rem !important;
  margin-bottom: 1rem !important;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
}

h2 {
  font-size: 1.8rem !important;
  margin: 1.5rem 0 1rem 0 !important;
}

h3 {
  font-size: 1.4rem !important;
  color: var(--primary-color) !important;
  margin: 1.2rem 0 0.8rem 0 !important;
}

.stSubheader {
  color: var(--primary-color) !important;
  font-weight: 700 !important;
  font-size: 1.3rem !important;
  padding: 1rem !important;
  background: linear-gradient(90deg, rgba(108, 99, 255, 0.15) 0%, transparent 100%) !important;
  border-left: 4px solid var(--primary-color) !important;
  border-radius: 6px !important;
  margin: 1.5rem 0 1rem 0 !important;
}

p {
  color: var(--text-secondary) !important;
  font-size: 1rem !important;
}

/* ============================================
   ALERT MESSAGES STYLING
   ============================================ */

[data-testid="stAlert"] {
  border-radius: 10px !important;
  padding: 1.2rem !important;
  margin: 1rem 0 !important;
  border-left: 4px solid !important;
  animation: slideIn 0.4s ease-out !important;
}

.stSuccess {
  background-color: rgba(0, 212, 255, 0.1) !important;
  border-color: var(--success-color) !important;
  color: #00D4FF !important;
}

.stSuccess > div > p {
  color: #00D4FF !important;
}

.stError {
  background-color: rgba(255, 107, 107, 0.1) !important;
  border-color: var(--error-color) !important;
  color: #FF6B6B !important;
}

.stError > div > p {
  color: #FF6B6B !important;
}

.stWarning {
  background-color: rgba(255, 217, 61, 0.1) !important;
  border-color: var(--warning-color) !important;
  color: #FFD93D !important;
}

.stWarning > div > p {
  color: #FFD93D !important;
}

.stInfo {
  background-color: rgba(108, 99, 255, 0.1) !important;
  border-color: var(--primary-color) !important;
  color: var(--primary-color) !important;
}

.stInfo > div > p {
  color: var(--primary-color) !important;
}

/* ============================================
   SPINNER/LOADING ANIMATION
   ============================================ */

[role="status"] {
  color: var(--primary-color) !important;
}

/* ============================================
   MAIN CONTAINER
   ============================================ */

[data-testid="stMainBlockContainer"] {
  padding: 2rem !important;
  max-width: 1200px !important;
}

.main {
  padding: 2rem !important;
}

/* ============================================
   VERTICAL BLOCKS & CARDS
   ============================================ */

[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
  background-color: rgba(28, 31, 38, 0.5) !important;
  border: 1px solid var(--border-color) !important;
  border-radius: 12px !important;
  padding: 1.5rem !important;
  margin: 1rem 0 !important;
  transition: all 0.3s ease !important;
}

[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"]:hover {
  border-color: var(--primary-color) !important;
  box-shadow: 0 8px 24px rgba(108, 99, 255, 0.15) !important;
  transform: translateY(-2px) !important;
}

/* ============================================
   MARKDOWN STYLING
   ============================================ */

.stMarkdown {
  color: var(--text-secondary) !important;
}

.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
  color: #FFFFFF !important;
}

/* ============================================
   CAPTION & TEXT STYLING
   ============================================ */

.stCaption {
  color: var(--text-secondary) !important;
  font-size: 0.85rem !important;
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
   ANIMATIONS
   ============================================ */

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

[data-testid="stForm"] {
  animation: slideUp 0.5s ease-out !important;
}

[data-testid="stAlert"] {
  animation: slideIn 0.4s ease-out !important;
}

/* ============================================
   RESPONSIVE DESIGN
   ============================================ */

@media (max-width: 768px) {
  h1 {
    font-size: 2rem !important;
  }

  h2 {
    font-size: 1.5rem !important;
  }

  h3 {
    font-size: 1.1rem !important;
  }

  .stForm {
    padding: 1.5rem !important;
  }

  [data-testid="stMainBlockContainer"] {
    padding: 1rem !important;
  }

  .stButton > button {
    padding: 14px 20px !important;
    font-size: 0.9rem !important;
  }

  .stSubheader {
    font-size: 1.1rem !important;
    padding: 0.8rem !important;
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 1.5rem !important;
  }

  [data-testid="stMainBlockContainer"] {
    padding: 0.5rem !important;
  }

  [data-testid="stForm"] {
    padding: 1rem !important;
  }
}

/* ============================================
   DOWNLOAD BUTTON STYLING
   ============================================ */

[data-testid="stDownloadButton"] > button {
  background: linear-gradient(135deg, #00D4FF 0%, #00A8CC 100%) !important;
  color: white !important;
  border: none !important;
  border-radius: 10px !important;
  padding: 12px 24px !important;
  font-weight: 600 !important;
  box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3) !important;
  transition: all 0.3s ease !important;
}

[data-testid="stDownloadButton"] > button:hover {
  background: linear-gradient(135deg, #00A8CC 0%, #0088AA 100%) !important;
  box-shadow: 0 6px 20px rgba(0, 212, 255, 0.5) !important;
  transform: translateY(-2px) !important;
}

</style>
""", unsafe_allow_html=True)


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

    # Form with submit button inside
    with st.form("mcq_form"):
        for idx, mcq in enumerate(mcqs):
            st.subheader(mcq['question'])
            options = mcq['choices']
            st.session_state.user_answers[idx] = st.radio(
                f"Select your answer for Question {idx+1}:",
                options,
                key=f"q_{idx}"
            )

        # Submit button placed inside the form block
        submitted = st.form_submit_button("Submit All Answers")
        if submitted:
            st.session_state.submitted = True

    # Evaluation
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

    # Export option
    if st.button("Export to DOC"):
        doc_buffer = export_to_doc(mcqs)
        st.download_button(
            label="Download DOC",
            data=doc_buffer,
            file_name="mcqs.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )


def main():
    # Page Config
    st.set_page_config(
        page_title="Quiz O Mania",
        page_icon="🧠",
        layout="wide"
    )

    # Sidebar UI
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

    # Main Area
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
