THEME_COLOR = "#375362"
import tkinter
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.quest = self.canvas.create_text(150, 125, text=self.quiz.next_question(), font=("Arial", 20, "italic"), width=280)

        right = tkinter.PhotoImage(file="./images/true.png")
        self.true = tkinter.Button(image=right, highlightthickness=0, command=self.yes)
        self.true.grid(column=0, row=2, padx=20, pady=20)


        wrong = tkinter.PhotoImage(file="./images/false.png")
        self.false = tkinter.Button(image=wrong, highlightthickness=0, command=self.no)
        self.false.grid(column=1, row=2, padx=20, pady=20)
        

        self.score = tkinter.Label(text=f"Score: {0}", bg=THEME_COLOR, foreground="white", font=("Arial", 15, "italic"))
        self.score.grid(column=1, row=0, padx=20, pady=20)


        self.window.mainloop()
    

    def update_bg(self, color):
        self.canvas.configure(bg=color)

    def new_quest(self):
            self.update_bg("white")
            self.canvas.itemconfig(self.quest, text=self.quiz.next_question())

    def score_update(self):
        self.score.config(text=f"Score: {self.quiz.score}")

    def no(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer(answer="False")
            self.score_update()
            self.update_bg(self.quiz.color)
            self.window.after(1000, self.new_quest)
        else:
            self.canvas.itemconfig(self.quest, text="You`ve reached the end of the quiz")


    def yes(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer(answer="True")
            self.score_update()
            self.update_bg(self.quiz.color)
            self.window.after(1000, self.new_quest)
        else:
            self.canvas.itemconfig(self.quest, text="You`ve reached the end of the quiz")