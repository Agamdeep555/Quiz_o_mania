import gradio as gr

# Function to generate multiple-choice questions
def generate_mcqs(topic, difficulty):

    # 🔹 EASY QUESTIONS
    if difficulty == "Easy":
        mcqs = [
            {
                "question": "What type of plot is used to show frequencies of numerical data?",
                "choices": ["Bar chart", "Histogram", "Scatter plot", "Pie chart"],
                "answer": "Histogram"
            },
            {
                "question": "Which probability approach is based on equally likely outcomes?",
                "choices": ["Classical", "Empirical", "Subjective", "Relative frequency"],
                "answer": "Classical"
            }
        ]

    # 🔹 MEDIUM QUESTIONS
    elif difficulty == "Medium":
        mcqs = [
            {
                "question": "Which probability approach is used in large survey-based experiments?",
                "choices": ["Classical approach", "Relative frequency approach", "Subjective approach", "Theoretical approach"],
                "answer": "Relative frequency approach"
            },
            {
                "question": "Which distribution is commonly used in medical trials?",
                "choices": ["Normal", "Poisson", "Binomial", "Exponential"],
                "answer": "Binomial"
            }
        ]

    # 🔹 HARD QUESTIONS
    else:
        mcqs = [
            {
                "question": "If Y = 3X − 2 and X ~ N(2, 4), what is the mean of Y?",
                "choices": ["2", "4", "6", "8"],
                "answer": "6"
            },
            {
                "question": "Which transformation is used when Y = βX and X follows a Gamma distribution?",
                "choices": ["Linear transformation", "Non-linear transformation", "Affine transformation", "Gamma transformation"],
                "answer": "Linear transformation"
            }
        ]

    # Format output
    output = f"📘 Topic: {topic}\n🎯 Difficulty: {difficulty}\n\n"
    for i, mcq in enumerate(mcqs, 1):
        output += f"{i}. {mcq['question']}\n"
        for j, choice in enumerate(mcq['choices'], 1):
            output += f"   {j}) {choice}\n"
        output += f"✅ Answer: {mcq['answer']}\n\n"

    return output


# Gradio Interface
iface = gr.Interface(
    fn=generate_mcqs,
    inputs=[
        gr.Textbox(label="Enter Topic"),
        gr.Dropdown(
            choices=["Easy", "Medium", "Hard"],
            label="Select Difficulty",
            value="Easy"
        )
    ],
    outputs=gr.Textbox(label="Generated MCQs"),
    title="Quiz-N-learn",
    description="Generate MCQs based on topic and difficulty level."
)

# Launch app
iface.launch()
