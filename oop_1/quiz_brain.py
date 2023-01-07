class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0 
        self.question_list = q_list  
        self.score = 0 
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1   
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(answer, question.answer)


    def still_has_questions(self):
        return self.question_number < len(self.question_list) 

    def check_answer(self, answer, question_answer):
        if answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1 
            print(f"You score its {self.score}/{self.question_number}")
        else:
            print("Thats wrong")
            print(f"Right answer was: {question_answer}") 
            print(f"You score its {self.score}/{self.question_number}")

    def final(self):
        print(f"You done, u final score is: {self.score}/{self.question_number}")

