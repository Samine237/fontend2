from tkinter import *
from tkinter import messagebox
from GUI.login import PlayerForm


def questionsquiz():
    window = Tk()
    window.title("Quiz")
    window.geometry("850x530")

    global user_answer
    user_answer = StringVar()

    global canvas
    canvas = Canvas(window, width=800, height=250)
    global question_text
    question_text = canvas.create_text(400, 30, text="Ici la premiere question a poser", width=680, font=('Ariel', 15, 'italic'))
    canvas.grid(row=2, column=0, columnspan=2, pady=50)


    next_button = Button(window, text="Answer",
                         width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
    next_button.place(x=450, y=460)

    choice_list = []

    # position of the first option
    y_pos = 220

    # adding the options to the list
    while len(choice_list) < 4:
        # setting the radio button properties
        radio_btn = Radiobutton(window, text="Ici le premier choix", variable=user_answer,
                                value='', font=("ariel", 14))

        # adding the button to the list
        choice_list.append(radio_btn)

        # placing the button
        radio_btn.place(x=200, y=y_pos)



    window.mainloop()


questionsquiz()