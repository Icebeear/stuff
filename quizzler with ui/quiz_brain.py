import html
class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0 
        self.question_list = q_list  
        self.score = 0 
        self.color = None
    
    def next_question(self):
        global question
        question = self.question_list[self.question_number]
        self.question_number += 1   
        return (f"Q.{self.question_number}: {html.unescape(question.text)}")


    def still_has_questions(self):
        return self.question_number < len(self.question_list) 

    def check_answer(self, answer):
        if answer == question.answer:
            self.score += 1
            self.color = "green"
        else:
            self.color = "red"


    def final(self):
        print(f"You done, u final score is: {self.score}/{self.question_number}")