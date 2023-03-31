from quiz_brain import QuizBrain
from tkinter import *
from tkinter import messagebox

THEME_COLOR = 'blue'

class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QUANTUM QUIZ")
        self.window.geometry("850x530")

        # Display title
        self.display_title()

        # A canvas for question text and displaying the question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125, text="Question here", width=680, fill=THEME_COLOR, font=('Ariel', 15, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Store user's answer
        self.user_answer = StringVar()

        # Disply four options (radio_buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.window, pady=10, font=('ariel', 15, 'bold'))
        self.feedback.place(x=290, y=50)

        # Next and Quit buttons
        self.buttons()
        self.window.mainloop(0)

    # DISPLAY THE TITLE
    def display_title(self):
        title = Label(self.window, text="QUANTUM QUIZ APPLICATION", width=50, bg='green', fg='crimson', font=('ariel', 20, 'bold'))
        title.place(x=0, y=2)

    # DISPLAY THE QUESTIONS
    def display_question(self):
        quest_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=quest_text)

    # CREATE THE RADIO BUTTONS
    def radio_buttons(self):
        choices = []  # empty options initialized
        y_position = 220   # position of the first option

        # Add the options to the list
        while len(choices) < 4:
            radio_button = Radiobutton(self.window, text="", variable=self.user_answer, value="", font=('ariel', 14))
            choices.append(radio_button)
            radio_button.place(x=200, y=y_position) # place the button(s)
            y_position += 41  # incrementing the position of the first question every time a new choice is added in
        return choices
    
    # DISPLAY THE OPTIONS
    def display_options(self):
        val = 0
        # deselecting the options
        self.user_answer.set(None)

        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    #  NEXT BUTTON FUNCTIONALITY 
    def next_button(self):
        # check if the answer given by the user is correct
        if (self.quiz.check_answer(self.user_answer.get())):
            self.feedback['fg'] = 'green'
            self.feedback['text'] = 'Correct! \U0001F44D'

        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                        f'The right answer is: {self.quiz.current_question.correct_answer}')
            
        if self.quiz.has_more_questions():
            # Move on the next one to display the next question, if there are any more
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then display the result
            self.display_result()   
            self.window.destroy()

    def buttons(self):
        """To show next button and quit button"""

        # The first button is the Next button to move to the next Question
        next_button = Button(self.window, text="Next", command=self.next_button,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # palcing the button on the screen
        next_button.place(x=350, y=460)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700, y=50)

    # DISPLAY THE RESULT
    def display_result(self):
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct : {correct}"
        wrong = f"Wrong : {wrong}"
        correct_percent = f"Percentage : {score_percent}"

        # Show a message box to display the result
        messagebox.showinfo(title="RESULT", message=f"\n{correct_percent}\n{correct}\n{wrong}")