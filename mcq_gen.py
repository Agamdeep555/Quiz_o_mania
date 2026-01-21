def generate_mcqs(text, difficulty):
    """
    Generates MCQs based on difficulty level.
    """

    if difficulty == "Easy":
        mcqs = [
            {
                "question": "What is probability?",
                "choices": [
                    "Study of random events",
                    "Study of geometry",
                    "Study of numbers",
                    "Study of functions"
                ],
                "answer": "Study of random events",
                "explanation": "Probability deals with uncertainty and randomness."
            }
        ]

    elif difficulty == "Medium":
        mcqs = [
            {
                "question": "Which probability approach is used in opinion polls?",
                "choices": [
                    "Classical",
                    "Relative frequency",
                    "Subjective",
                    "Axiomatic"
                ],
                "answer": "Relative frequency",
                "explanation": "Polling uses experimental data and long-run frequency."
            }
        ]

    else:  # Hard
        mcqs = [
            {
                "question": "If X ~ N(2, 4), what is the mean of Y = 3X − 2?",
                "choices": ["2", "4", "6", "8"],
                "answer": "6",
                "explanation": "Mean transforms linearly: 3×2 − 2 = 6."
            }
        ]

    return mcqs
