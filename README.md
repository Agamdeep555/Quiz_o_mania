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
   ![image](https://github.com/user-attachments/assets/76ee41f3-10ea-4871-9aa3-4e1884a0c09f)
2) Evaluates the quiz and shows the final score
   ![image](https://github.com/user-attachments/assets/8bfde1ca-41c8-42f6-b010-240c367114e5)
   ![image](https://github.com/user-attachments/assets/318dfc68-8aab-4d91-9d7b-ceff192cd41e)
3) Option to download for further revision
   ![image](https://github.com/user-attachments/assets/43bab416-d00f-4c0b-baa2-c95014fd85be)



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
Kashish Seth
📧 Email: kseth9852@gmail.com

For queries, support, or collaboration — feel free to reach out!
