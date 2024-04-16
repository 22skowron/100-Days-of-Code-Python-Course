import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ") # Change text displayed in text widget
        # self.check_answer(user_answer)

    def check_answer(self, user_answer): # green/red button --> command=check_answer, "True"/"False"
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower(): # lower can be omitted
            self.score += 1 # Display upgraded score

            return True
            # print("You got it right!") # change canvas bg to green
        else:
            return False
            # print("That's wrong.") # change canvas bg to red

        # print(f"Your current score is: {self.score}/{self.question_number}") # wait 3 sec and initialize new question
        # print("\n") # 123

    # def change_color(self):
    #     interface.change_cv_color()