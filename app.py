import sys

LESSONS = {
    "1": {
        "title": "HTML5 Basics",
        "summary": "Learn semantic tags, media elements, and form improvements.",
        "example": """<header><nav>Menu</nav></header>\n<main><section><article>Content</article></section></main>""",
        "explanation": "Semantic elements make pages easier to understand for both browsers and developers."
    },
    "2": {
        "title": "CSS3 Basics",
        "summary": "Learn colors, backgrounds, borders, shadows, and typography.",
        "example": "body { background: linear-gradient(#f4f4f4, #ddd); border-radius: 12px; }",
        "explanation": "CSS3 styles the page and adds modern visual effects without changing HTML structure."
    },
    "3": {
        "title": "Layouts and Responsiveness",
        "summary": "Learn Flexbox, Grid, and media queries for adaptive layouts.",
        "example": "@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }",
        "explanation": "Responsive design allows webpages to adapt to different screen sizes and devices."
    },
    "4": {
        "title": "Advanced Features",
        "summary": "Learn animations, transitions, transforms, and CSS variables.",
        "example": "@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }",
        "explanation": "Advanced CSS creates polished and dynamic user experiences."
    }
}


def print_header():
    print("\n=== HTML5 & CSS3 Learning Tool ===")
    print("Choose an option:\n")
    for key, lesson in LESSONS.items():
        print(f"{key}. {lesson['title']} - {lesson['summary']}")
    print("9. Quick quiz")
    print("0. Exit")


def print_lesson(choice):
    lesson = LESSONS.get(str(choice))
    if not lesson:
        print("Invalid lesson selection.")
        return

    print(f"\n--- {lesson['title']} ---")
    print(lesson['summary'])
    print("\nExplanation:")
    print(lesson['explanation'])
    print("\nExample:")
    print(lesson['example'])


def run_quiz():
    questions = [
        {
            "question": "Which HTML5 element is best for a self-contained article such as a blog post?",
            "options": ["<section>", "<article>", "<div>", "<span>"],
            "answer": "<article>"
        },
        {
            "question": "Which CSS property creates rounded corners?",
            "options": ["padding", "border-radius", "margin", "text-shadow"],
            "answer": "border-radius"
        },
        {
            "question": "Which CSS feature is best for creating flexible item layouts in rows and columns?",
            "options": ["Flexbox", "Float", "Position: static", "Text-align"],
            "answer": "Flexbox"
        }
    ]

    score = 0
    print("\n--- Quick Quiz ---")
    for index, q in enumerate(questions, start=1):
        print(f"\nQ{index}: {q['question']}")
        for option in q['options']:
            print(f"- {option}")

        user_answer = input("Your answer: ").strip()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['answer']}")

    print(f"\nYour score: {score}/{len(questions)}")


def main():
    while True:
        print_header()
        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Thanks for learning! See you next time.")
            sys.exit(0)
        elif choice == "9":
            run_quiz()
        elif choice in LESSONS:
            print_lesson(choice)
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
