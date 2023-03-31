from quiz_model import Question
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from quiz_data import question_data
from random import shuffle

def main():
    question_bank = []
    for question in question_data:
        choices = []
        question_text = question['question']
        correct_answer = question['correct_answer']
        incorrect_answers = question['incorrect_answers']
        for ans in incorrect_answers:
            choices.append(ans)
        choices.append(correct_answer)
        shuffle(choices)
        new_question = Question(question=question_text, correct_answer=correct_answer, options=choices)
        question_bank.append(new_question)

    quiz = QuizBrain(questions=question_bank)
    quiz_ui = QuizInterface(quiz_brain=quiz)

    print("You have completed the Quantum Quiz!! Congratulations!")
    print(f"You final score is: {quiz.score}/{quiz.question_no}")

# if __name__ == "__main__":
#     main()