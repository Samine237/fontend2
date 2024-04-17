from tkinter import *
from tkinter import messagebox
from GUI.login import PlayerForm
from GUI.quetions import questionsquiz


def start_quiz():
    window = Tk()
    window.title("Quiz")
    window.geometry("850x530")

    global user_answer
    user_answer = StringVar()

    global canvas
    canvas = Canvas(window, width=800, height=250)
    global question_text
    question_text = canvas.create_text(400, 30, text="Choice your category", width=680, font=('Ariel', 15, 'italic'))
    canvas.grid(row=2, column=0, columnspan=2, pady=50)
    cat1 = Button(window, text="History", command=questionsquiz, width=20, bg="black", fg="white", font=("ariel", 16, "bold"))
    cat1.place(x=150, y=150)

    cat2 = Button(window, text="Geography", width=20, bg="black", fg="white", font=("ariel", 16, "bold"))
    cat2.place(x=450, y=150)

    cat3 = Button(window, text="Sport", width=20, bg="black", fg="white", font=("ariel", 16, "bold"))
    cat3.place(x=150, y=250)

    cat4 = Button(window, text="Maths", width=20, bg="black", fg="white", font=("ariel", 16, "bold"))
    cat4.place(x=450, y=250)

    next_button = Button(window, text="Next",
                         width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
    next_button.place(x=450, y=460)

    inscr = Button(window, text="login", command=PlayerForm, width=5, bg="green", fg="white", font=("ariel", 16, " bold"))
    inscr.place(x=350, y=460)

    quit_button = Button(window, text="Quit", command=window.destroy, width=5, bg="red", fg="white", font=("ariel", 16, " bold"))
    quit_button.place(x=250, y=460)

    window.mainloop()


start_quiz()
