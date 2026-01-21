# 📚 Quiz-N-Learn: PDF-Based MCQ Generator

**Quiz-O-Mania** is an AI-powered Streamlit web app that generates multiple-choice questions (MCQs) from any uploaded PDF document.  
It helps students, educators, and professionals quickly create quizzes and test their knowledge with AI-evaluated answers and explanations.

---

## ✨ Features

🚀 Key Features

✅ Upload any PDF (lecture notes, reports, research papers, etc.)
✅ Generate AI-based MCQs directly from the document
✅ Choose difficulty level: Easy / Medium / Hard
✅ Each question includes:
4 answer options
Correct answer
Short explanation
✅ Interactive quiz interface
✅ Automatic score calculation
✅ Export MCQs to DOCX for offline revision
✅ Light / Dark mode UI
✅ Clean, modern, responsive design
✅ Powered by **LangChain + Groq LLM**

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
   git clone https://github.com/your-username/quiz-n-learn.git
   
   cd quiz-n-learn
```
### 2. Install Dependencies
```bash
 -pip install -r requirements.txt
```
### 3. Add Groq API Key
```bash
 -Create a .streamlit/secrets.toml file and add:

GROQ_API_KEY = "your-groq-api-key-here"
```
💡 Get your API key from: https://console.groq.com/keys

### 4. Run the App
```bash
 -streamlit run app.py
```


### Screenshot
1) Uploading the document
   <img width="1913" height="864" alt="Screenshot 2026-01-21 191938" src="https://github.com/user-attachments/assets/66c27a64-be0e-4fa4-b896-184d30faffaf" />

2) Evaluates the quiz and shows the final score
   <img width="1908" height="852" alt="Screenshot 2026-01-21 192153" src="https://github.com/user-attachments/assets/d070f32a-3d49-4cb0-be52-3ee9b9c0ab08" />

   <img width="1904" height="850" alt="Screenshot 2026-01-21 192327" src="https://github.com/user-attachments/assets/19a3b246-e395-4b44-9ffc-014f1726d825" />

3) Option to download for further revision
   <img width="404" height="188" alt="Screenshot 2026-01-21 192220" src="https://github.com/user-attachments/assets/a82928d9-7328-4103-ab64-a04d4324fce2" />




### 💡 Use Cases
1. 📖 Self-study from lecture PDFs 

2. 🏥 Generating quizzes from document


3. 📑 Generating scores for analysis.
   
4. 👨‍🏫 Teaching assistants auto-generating tests


### 🛠 Built With
🐍 Python

🔥 LangChain

🤖 Groq (LLaMA3-70B model)

🧠 Streamlit

📄 PyPDF2

📤 python-docx

### 👩‍💻 Author
Agamdeep Singh
agamdeepsingh555@gmail.com

For queries, support, or collaboration — feel free to reach out!
