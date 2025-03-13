from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    ques_ans = Question(question["text"], question["answer"])
    question_bank.append(ques_ans)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

if not quiz.still_has_question():
    print("\nThe quiz has ended!")
    print(f"Your final score is {quiz.score}.")
