from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []

for key in question_data:
    question_bank.append(Question(key["question"], key["correct_answer"]))


quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)