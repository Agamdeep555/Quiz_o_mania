# 🧠 Quiz O Mania - AI-Powered MCQ Generator

> **Transform PDFs into Interactive Quizzes Instantly** with AI-powered multiple-choice question generation

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with ❤️ by Agamdeep Singh](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20by-Agamdeep%20Singh-purple)](https://github.com/agamdeepsingh)

---

## 🎯 Overview

**Quiz O Mania** is a cutting-edge Streamlit web application that leverages AI to automatically generate high-quality multiple-choice questions (MCQs) from PDF documents. Perfect for students, educators, and professionals who want to create engaging quizzes and assessments in minutes.

### Why Quiz O Mania?
- ⚡ **Instant Quiz Creation** - Generate MCQs in seconds
- 🎓 **Adaptive Difficulty** - Choose Easy, Medium, or Hard
- 🤖 **AI-Powered** - Powered by Groq's LLaMA3-70B LLM
- 📊 **Smart Evaluation** - Get instant scores with detailed explanations
- 📥 **Export Ready** - Download as DOCX for offline use
- 🎨 **Modern UI** - Beautiful dark theme with smooth animations
- 📱 **Responsive Design** - Works seamlessly on all devices

---

## ✨ Key Features

### 📄 **PDF Processing**
- Upload any PDF document (lecture notes, research papers, textbooks, etc.)
- Intelligent text extraction and processing
- Support for large documents (up to 200MB)

### 🧠 **Smart MCQ Generation**
- AI-generated questions with context-aware answers
- 4 multiple-choice options per question
- Difficulty-based question generation
- Auto-generated explanations for learning

### 📊 **Interactive Quiz Interface**
- Clean, intuitive question display
- Single-select radio button interface
- Real-time progress tracking
- Instant submission and evaluation

### 🎯 **Score Evaluation**
- Automatic answer verification
- Detailed result breakdown
- Explanation for each answer
- Final score display with performance metrics

### 💾 **Export & Share**
- Download MCQs as Word documents (.DOCX)
- Ready-to-print format
- Perfect for offline study and sharing

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Groq API Key (free at [console.groq.com](https://console.groq.com/keys))

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/agamdeepsingh/quiz-o-mania.git
cd quiz-o-mania
```

#### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure API Key

Create a file `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your-groq-api-key-here"
```

Get your free API key from: https://console.groq.com/keys

#### 5. Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📖 How to Use

### Step 1: Upload PDF
- Click "Upload a PDF" in the sidebar
- Select your document (PDF format)
- Wait for processing confirmation

### Step 2: Choose Difficulty
- Select from three difficulty levels:
  - 🟢 **Easy** - Straightforward questions
  - 🟡 **Medium** - Balanced complexity
  - 🔴 **Hard** - Challenging questions

### Step 3: Take the Quiz
- Read each question carefully
- Select your answer from the options
- Review all answers before submitting

### Step 4: Check Results
- Submit all answers
- View instant feedback
- Read explanations for each answer
- See your final score

### Step 5: Export (Optional)
- Click "Export to DOC"
- Download MCQs as a Word document
- Use for offline study or sharing

---

## 📸 Screenshots

### 1️⃣ Dashboard
![Quiz O Mania Dashboard](https://github.com/user-attachments/assets/66c27a64-be0e-4fa4-b896-184d30faffaf)

*Clean interface with PDF upload and difficulty selection*

### 2️⃣ Quiz Interface
![Quiz Interface](https://github.com/user-attachments/assets/d070f32a-3d49-4cb0-be52-3ee9b9c0ab08)

*Interactive question display with answer options*

### 3️⃣ Results & Evaluation
![Results Page](https://github.com/user-attachments/assets/19a3b246-e395-4b44-9ffc-014f1726d825)

*Detailed evaluation with explanations and score*

### 4️⃣ Export Option
![Export Button](https://github.com/user-attachments/assets/a82928d9-7328-4103-ab64-a04d4324fce2)

*Download MCQs for offline use*

---

## 🏗️ Project Structure

```
quiz-o-mania/
│
├── 📄 app.py                 # Main Streamlit application
├── 🎨 app.css                # Custom styling
├── 🤖 generate.py            # MCQ generation logic
├── 📥 export.py              # DOCX export functionality
├── 🛠️ utils.py               # PDF text extraction
│
├── 📋 requirements.txt        # Python dependencies
├── 📖 README.md             # This file
├── 📄 .gitignore            # Git ignore rules
│
└── 📁 .streamlit/
    └── 🔐 secrets.toml      # API keys (not tracked)
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web framework & UI |
| **LangChain** | LLM orchestration & chains |
| **Groq API** | LLaMA3-70B LLM inference |
| **PyPDF2** | PDF text extraction |
| **python-docx** | DOCX file generation |

---

## 💡 Use Cases

### 📚 **For Students**
- Create practice quizzes from lecture notes
- Self-assessment before exams
- Generate multiple versions for revision
- Export for group study sessions

### 👨‍🏫 **For Educators**
- Auto-generate assessments from course materials
- Create quick formative assessments
- Generate difficulty-varied question banks
- Reduce time spent on test creation

### 📖 **For Content Creators**
- Extract key concepts from documents
- Generate study materials
- Create interactive learning resources
- Build comprehensive question databases

### 🏢 **For Professionals**
- Create training assessment materials
- Generate certification prep questions
- Extract key insights from reports
- Build knowledge testing systems

---

## ⚙️ Configuration

### Environment Variables
```bash
GROQ_API_KEY        # Required: Your Groq API key
```

### Customize Number of Questions

Edit `app.py`:
```python
# Change this value to generate different number of questions
NUM_QUESTIONS = 10
```

### Customize Difficulty Prompts

Edit `generate.py`:
```python
DIFFICULTY_PROMPTS = {
    "Easy": "Generate simple questions...",
    "Medium": "Generate moderate questions...",
    "Hard": "Generate challenging questions..."
}
```

---

## 🐛 Troubleshooting

### ❌ Issue: "API Key not found"
**Solution:** 
```bash
# Make sure .streamlit/secrets.toml exists with:
GROQ_API_KEY = "your-key-here"
```

### ❌ Issue: "Failed to generate MCQs"
**Solution:** 
- Ensure PDF has sufficient text content (>500 characters)
- Verify API key is valid
- Check internet connection
- Try with a different PDF file

### ❌ Issue: "PDF extraction failed"
**Solution:**
- Ensure PDF is not password-protected
- Try a different PDF file
- Check if file is not corrupted
- Verify PDF contains text (not scanned images)

### ❌ Issue: "Slow response time"
**Solution:**
- Groq API is optimized but may vary by load
- Reduce number of questions
- Check internet connection speed
- Wait a moment and retry

---

## 📦 Requirements

```
streamlit==1.31.0
langchain==0.1.0
groq==0.4.1
python-docx==0.8.11
PyPDF2==3.0.1
python-dotenv==1.0.0
```

### Install All Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Security & Privacy

- ✅ API keys stored locally in `.streamlit/secrets.toml`
- ✅ PDF files processed temporarily and not stored permanently
- ✅ No personal data collection or tracking
- ✅ Open-source and fully transparent
- ✅ All processing happens on secure Groq servers

### Important Security Notes
```bash
# Never commit secrets to git!
# Add to .gitignore:
.streamlit/secrets.toml

# Keep your API key confidential
# Use environment variables in production
```

---

## 🚀 Deployment

### Deploy on Streamlit Cloud (Recommended)

1. Push code to GitHub:
```bash
git push origin main
```

2. Visit [share.streamlit.io](https://share.streamlit.io)

3. Click "New app" and connect your GitHub repository

4. Add secrets in the app's Secrets section:
```toml
GROQ_API_KEY = "your-key-here"
```

5. Deploy with one click!

### Deploy on Other Platforms

**Railway:**
```bash
# Push to Railway
railway up
```

**Heroku:**
```bash
# Deploy using Heroku CLI
heroku create your-app-name
git push heroku main
```

**Docker (Any Cloud):**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

---

## 📈 Performance Metrics

| Operation | Time |
|-----------|------|
| PDF Processing | < 2 seconds |
| MCQ Generation | 5-10 seconds |
| Quiz Evaluation | Instant |
| Export to DOCX | < 1 second |
| Average Response | 8-12 seconds |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
```bash
git fork https://github.com/agamdeepsingh/quiz-o-mania.git
```

2. Create a feature branch
```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes
```bash
git commit -m 'Add amazing feature'
```

4. Push to the branch
```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

### Development Setup
```bash
# Install with dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Format code
black .
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Agamdeep Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 👨‍💻 Author & Contact

### Agamdeep Singh

- 🔗 **GitHub:** [@agamdeepsingh](https://github.com/agamdeepsingh)
- 📧 **Email:** [agamdeepsingh555@gmail.com](mailto:agamdeepsingh555@gmail.com)
- 💼 **LinkedIn:** [Agamdeep Singh](https://linkedin.com/in/agamdeepsingh)
- 🐦 **Twitter:** [@agamdeepsingh](https://twitter.com/agamdeepsingh)

### Get Help
- 📧 **Email:** agamdeepsingh555@gmail.com
- 🐛 **Report Bug:** [GitHub Issues](https://github.com/agamdeepsingh/quiz-o-mania/issues)
- 💬 **Discuss:** [GitHub Discussions](https://github.com/agamdeepsingh/quiz-o-mania/discussions)
- 📱 **Contact Form:** [Coming Soon]

---

## ⭐ Show Your Support

If you find Quiz O Mania helpful, please consider:

- ⭐ **Star** this repository on GitHub
- 🐛 **Report bugs** and **suggest features**
- 📢 **Share** with friends and colleagues
- 🤝 **Contribute** improvements
- 💬 **Leave feedback** on discussions

---

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [LangChain Docs](https://python.langchain.com)
- [Groq API Guide](https://console.groq.com/docs)
- [Python-docx Tutorial](https://python-docx.readthedocs.io)
- [PyPDF2 Documentation](https://pypdf.readthedocs.io)

---

## 🎓 Related Projects

- [PDF2Quiz](https://github.com/user/pdf2quiz) - Similar project
- [QuizMaker](https://github.com/user/quizmaker) - Alternative solution
- [LangChain Examples](https://github.com/langchain-ai/langchain) - Official examples

---

## 📞 Feedback & Suggestions

Your feedback helps us improve! Share your thoughts:

- 🎯 **Feature Requests:** [GitHub Issues](https://github.com/agamdeepsingh/quiz-o-mania/issues)
- 💡 **Suggestions:** [Discussions](https://github.com/agamdeepsingh/quiz-o-mania/discussions)
- 🐛 **Bug Reports:** [Issues](https://github.com/agamdeepsingh/quiz-o-mania/issues)
- 📧 **Direct Contact:** agamdeepsingh555@gmail.com

---

## 🔄 Changelog

### Version 1.0.0 (Current)
- ✅ Initial release
- ✅ PDF upload functionality
- ✅ AI MCQ generation
- ✅ Interactive quiz interface
- ✅ DOCX export feature
- ✅ Dark theme UI
- ✅ Responsive design

### Coming Soon
- 🚀 Light theme support
- 🚀 Multiple language support
- 🚀 Image-based questions
- 🚀 Performance analytics
- 🚀 User authentication
- 🚀 Question bank management

---

## ❓ FAQ

**Q: Is this free to use?**
A: Yes! Quiz O Mania is free and open-source. You just need a free Groq API key.

**Q: What file formats are supported?**
A: Currently, only PDF files are supported. More formats coming soon!

**Q: Can I use this commercially?**
A: Yes, under the MIT license. See the LICENSE file for details.

**Q: How many questions are generated?**
A: By default, 10 questions per PDF. You can customize this in `app.py`.

**Q: Is my data secure?**
A: Yes! PDFs are processed temporarily and not stored permanently.

**Q: Can I deploy this on my own server?**
A: Yes! Follow the deployment instructions above.

---

<div align="center">

## 🌟 Made with ❤️ by [Agamdeep Singh](https://github.com/agamdeepsingh)

⭐ **If you found this helpful, please star the repository!** ⭐

[⬆ Back to Top](#-quiz-o-mania---ai-powered-mcq-generator)

</div>
