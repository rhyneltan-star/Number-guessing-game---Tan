from tkinter import *
import random

# ================= WINDOW ================= #
root = Tk()
root.title("Mystery Number Quest")
root.geometry("700x550")
root.config(bg="#0f0f0f")

# ================= GAME DATA ================= #
max_number = 10
secret_number = 0
lives = 5
score = 10

wrong_messages = [
    "🤖 Wrong guess!",
    "👾 Access denied!",
    "💀 Try again!",
    "⚠️ Incorrect!"
]

win_messages = [
    "🏆 Mission Complete!",
    "🎉 You cracked the code!",
    "🚀 Victory!"
]

# ================= START GAME ================= #
def start_game():
    global secret_number, lives, score

    secret_number = random.randint(1, max_number)

    lives = 5
    score = 10

    lives_label.config(text=f"❤️ Lives: {lives}")
    score_label.config(text=f"⭐ Score: {score}/10")

    result.config(text="🎮 Game Started!", fg="white")

    root.config(bg="#0f0f0f")

    guess_entry.config(state=NORMAL)
    check_btn.config(state=NORMAL)

# ================= CHECK GUESS ================= #
def check_guess():
    global lives, score

    guess = guess_entry.get()

    # Check if input is a number
    if not guess.isdigit():
        result.config(text="⚠️ Enter numbers only!", fg="yellow")
        return

    guess = int(guess)

    # Check valid range
    if guess < 1 or guess > max_number:
        result.config(text="Please enter numbers 1-10 only!", fg="orange")
        return

    # ===== CORRECT ===== #
    if guess == secret_number:

        result.config(
            text=f"{random.choice(win_messages)}\n⭐ Final Score: {score}/10",
            fg="#00ff99"
        )

        guess_entry.config(state=DISABLED)
        check_btn.config(state=DISABLED)

    # ===== WRONG ===== #
    else:
        lives -= 1
        score -= 2

        if score < 0:
            score = 0

        lives_label.config(text=f"❤️ Lives: {lives}")
        score_label.config(text=f"⭐ Score: {score}/10")

        hint = "📈 Higher!" if guess < secret_number else "📉 Lower!"

        result.config(
            text=f"{random.choice(wrong_messages)}\n{hint}",
            fg="#ff6666"
        )

        root.config(bg=random.choice([
            "#220000",
            "#1a1a2e",
            "#2d132c"
        ]))

        # Game Over
        if lives <= 0:

            result.config(
                text=f"💀 Game Over!\nNumber was {secret_number}",
                fg="red"
            )

            guess_entry.config(state=DISABLED)
            check_btn.config(state=DISABLED)

    guess_entry.delete(0, END)

# ================= RESTART ================= #
def restart_game():

    root.config(bg="#0f0f0f")

    result.config(
        text="🎮 Click Start Game",
        fg="white"
    )

    guess_entry.delete(0, END)

    guess_entry.config(state=DISABLED)
    check_btn.config(state=DISABLED)

# ================= TITLE ================= #
Label(
    root,
    text="💻 MYSTERY NUMBER QUEST",
    font=("Consolas", 24, "bold"),
    bg="#0f0f0f",
    fg="#00ff00"
).pack(pady=20)

# ================= START BUTTON ================= #
Button(
    root,
    text="Start Game",
    command=start_game,
    bg="#00aa00",
    fg="white",
    width=15
).pack()

# ================= LABELS ================= #
lives_label = Label(
    root,
    text="❤️ Lives: 5",
    bg="#0f0f0f",
    fg="#ff4d4d"
)
lives_label.pack()

score_label = Label(
    root,
    text="⭐ Score: 10/10",
    bg="#0f0f0f",
    fg="#ffd700"
)
score_label.pack()

# ================= ENTRY ================= #
guess_entry = Entry(
    root,
    font=("Consolas", 18),
    justify="center",
    width=10,
    state=DISABLED,
    bg="#1f1f1f",
    fg="#00ff00",
    insertbackground="#00ff00"
)
guess_entry.pack(pady=20)

# ================= BUTTONS ================= #
buttons = Frame(root, bg="#0f0f0f")
buttons.pack()

check_btn = Button(
    buttons,
    text="Guess",
    command=check_guess,
    state=DISABLED,
    bg="#0066ff",
    fg="white",
    width=12
)
check_btn.grid(row=0, column=0, padx=5)

Button(
    buttons,
    text="Restart",
    command=restart_game,
    bg="#00aa66",
    fg="white",
    width=12
).grid(row=0, column=1, padx=5)

# ================= RESULT ================= #
result = Label(
    root,
    text="🎮 Awaiting mission start...",
    font=("Arial", 14, "bold"),
    bg="#0f0f0f",
    fg="white"
)
result.pack(pady=40)

# ================= MAIN LOOP ================= #
root.mainloop()