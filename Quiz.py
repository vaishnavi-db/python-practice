questions = {
    "Capital of India?": "delhi",
    "2 + 2 * 2 = ?": "6",
    "Python creator?": "guido van rossum"
}

score = 0
for q, ans in questions.items():
    user_ans = input(q + " ").lower().strip()
    if user_ans == ans:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. Answer: {ans}")

print(f"\nFinal Score: {score}/{len(questions)}")
