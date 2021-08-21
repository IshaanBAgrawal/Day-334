from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.reps = 0
        self.quiz = quiz_brain
        self.user_answer = None
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Question",
                                                fill=THEME_COLOR,
                                                font=("Arial", 20, "italic")
                                                )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct = PhotoImage(file="images/true.png")
        self.correct_button = Button(
            image=correct,
            highlightthickness=0,
            border=1, bg=THEME_COLOR,
            command=self.user_answer_true
        )
        self.correct_button.grid(column=0, row=2)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(
            image=wrong,
            highlightthickness=0,
            border=1, bg=THEME_COLOR,
            command=self.user_answer_false
        )
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You have reached the end of the quiz. Your score is {self.quiz.score}/{self.quiz.question_number}")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def user_answer_true(self):
        self.user_answer = "True"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def user_answer_false(self):
        self.user_answer = "False"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        elif not is_correct:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
