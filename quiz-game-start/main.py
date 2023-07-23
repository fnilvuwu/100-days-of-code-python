from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

## in python question here is equal to question[0] so what happen is question[0]["text"]
for question in question_data:
    quiz_text = question["text"]
    quiz_answer = question["answer"]
    quiz = Question(quiz_text, quiz_answer)
    question_bank.append(quiz)

startquiz = QuizBrain(question_bank)

while startquiz.still_has_question():
    startquiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {startquiz.score}/{startquiz.question_number}")
