class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"\nQ.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, crct_answer):
        if user_answer.lower() == crct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's a wrong answer!")

        print(f"\nThe correct answer is {crct_answer}.")
        print(f"Your score: {self.score}")
