from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
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
        self.correct_button = Button(image=correct, highlightthickness=0, border=1, bg=THEME_COLOR)
        self.correct_button.grid(column=0, row=2)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0, border=1, bg=THEME_COLOR)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
