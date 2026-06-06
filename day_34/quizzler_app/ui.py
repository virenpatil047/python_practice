from tkinter import *
from pathlib import Path
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BASE = Path(__file__).parent

class QuizInterface:
    
    def __init__(self, quiz_brain : QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler", )
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(text="Score : 0 ", bg=THEME_COLOR)
        self.score.grid(row=0, column=1, padx=20, pady=20)
        
        self.card = Canvas(width=300, height=250, highlightthickness=0)
        self.question = self.card.create_text(150, 125, width=280, text="Q ", fill="black", font=("Ariel", 20, "italic"))
        self.card.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        
        true_image = PhotoImage(file=BASE / "images/true.png")
        self.true = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, command=self.check_answer_true)
        self.true.grid(row=2, column=0, padx=20, pady=20)
        
        false_image = PhotoImage(file=BASE / "images/false.png")
        self.false = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0, command=self.check_answer_false)
        self.false.grid(row=2, column=1, padx=20, pady=20)
        
        self.quiz = quiz_brain
        self.get_question()
        
        
        self.window.mainloop()
        
    def get_question(self):
        self.card.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.question, text= q_text)
        else:
            self.card.itemconfig(self.question, text= "You've reached end of the quiz !")
            self.false.config(command=DISABLED)
            self.true.config(command=DISABLED)
        
    def revert_color(self):
        self.card.config(bg="white")
    
    def after_answer(self, ans):
        if ans:
            self.card.config(bg="green")
        else:
            self.card.config(bg="red")
        self.window.after(1000, self.get_question)
    
    def check_answer_true(self):
        ans, score, q_count = self.quiz.check_answer("True")
        self.update_score(score, q_count)
        self.after_answer(ans)
    
    def check_answer_false(self):
        ans, score, q_count = self.quiz.check_answer("False")
        self.update_score(score, q_count)
        self.after_answer(ans)
    
    def update_score(self, score, q_count):
        self.score.config(text=f"Score : {score}/{q_count}")
        
    
