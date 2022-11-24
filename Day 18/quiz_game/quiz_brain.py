class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        num_of_questions = len(self.question_list)
        return self.question_number < num_of_questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_response = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_response, current_question.answer)

    def check_answer(self, user_response, correct_answer):
        if user_response.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
