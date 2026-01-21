

import streamlit as st
from generate import generate_mcqs
from export import export_to_doc
from utils import extract_text_from_pdf

st.markdown("""
<style>

/* 🌤 Main app background */
.stApp {
    background-color: #F6F8FC;
}

/* 🧭 Sidebar */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E5E7EB;
}

/* 📝 Titles */
h1, h2, h3 {
    color: #2C2F4A;
}

/* 📄 Question cards */
div[data-testid="stVerticalBlock"] > div {
    background-color: #FFFFFF;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 16px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.04);
}

/* 🔘 Buttons */
.stButton > button {
    background-color: #6C63FF;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #5750EC;
}

/* 🎯 Radio buttons */
.stRadio label {
    font-size: 16px;
    color: #374151;
}

/* 📦 Info / success boxes */
.stAlert {
    border-radius: 12px;
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

