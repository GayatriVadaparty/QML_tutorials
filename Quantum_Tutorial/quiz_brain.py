class QuizBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        return self.question_no < len(self.questions)
    
    def next_question(self):
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        ques_text = self.current_question.question_text
        return f"Q{self.question_no}. {ques_text}"
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1     # Increasing the score by one point for every correct answer
            return True
        else:
            # self.score -= 1   # Deducting a point for every wrong answer
            return False
        
    def get_score(self):
        wrong = self.question_no - self.score
        score_percent = int((self.score / self.question_no) * 100)
        return (self.score, wrong, score_percent)