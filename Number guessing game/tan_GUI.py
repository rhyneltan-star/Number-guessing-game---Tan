from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Number Guessing Game")

try:
    icon = PhotoImage(file="domo.ppm")
    root.iconphoto(True, icon)
except Exception as e:
    print(f"Icon error: {e}")


secret_number = random.randint(1, 10)

title_label = Label(root, text="Guess the Number (1-10)", font=("Arial", 14))
title_label.pack(pady=20)

guess_entry = Entry(root, font=("Arial", 12))
guess_entry.pack()

result_label = Label(root, text="")
result_label.pack(pady=20)


def check_guess():
    guess = guess_entry.get()

    if guess.isdigit():
        guess = int(guess)

        if guess == secret_number:
            result_label.config(text="Correct! You guessed the number!")
        else:
            result_label.config(text="Wrong guess! Try again.")
    else:
        result_label.config(text="Please enter a valid number!")

check_button = Button(root, text="Check Guess", command=check_guess)
check_button.pack(pady=10)

root.mainloop()