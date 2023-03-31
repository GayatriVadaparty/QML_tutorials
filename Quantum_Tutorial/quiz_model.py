class Question:
    def __init__(self, question : str, correct_answer : str, options : list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = options