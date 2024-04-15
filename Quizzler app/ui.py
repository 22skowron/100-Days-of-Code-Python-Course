from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=300, width=250)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        self.text_widget = self.canvas.create_text(125, 150,
                                                   text="default text",
                                                   font=("Arial", 12, "normal"),
                                                   width=230)

        self.lbl_score = Label(text="", font=("Arial", 12, "bold"), bg=THEME_COLOR)
        self.lbl_score.grid(row=1, column=2)

        self.tick_image = PhotoImage(file="images/true.png")
        self.btn_right = Button(image=self.tick_image, highlightthickness=0, bg=THEME_COLOR,
                                command=lambda: self.show_if_correct("True"))
        self.btn_right.grid(row=3, column=1)

        self.cross_image = PhotoImage(file="images/false.png")
        self.btn_wrong = Button(image=self.cross_image, highlightthickness=0, bg=THEME_COLOR,
                                command=lambda: self.show_if_correct("False"))
        self.btn_wrong.grid(row=3, column=2)



        self.display_next_question()
        self.window.mainloop()


    def display_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            text_to_display = self.quiz.next_question()
        else:
            text_to_display = "Finished"

        self.canvas.itemconfig(self.text_widget, text=text_to_display)



    def show_if_correct(self, answer):
        if self.quiz.question_number <= 10:

            if self.quiz.check_answer(answer):
                self.canvas.config(bg="green")
                self.lbl_score.config(text=f"Score: {self.quiz.score}")
            else:
                self.canvas.config(bg="red")

            self.canvas.after(500, self.display_next_question)

            if self.quiz.question_number == 10:
                self.quiz.question_number += 1

        else:
            pass






