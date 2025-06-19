import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x400")
        self.instruction = tk.Label(self.root, text="Select difficulty:", font=("Times New Roman", 14),bg="#f24329",fg="black")
        self.instruction.pack(pady=5)
        # Set background color instead of image
        self.root.configure(bg= "#f24329")
        self.difficulty_levels = {
            "Easy (1-50)": 50,
            "Medium (1-100)": 100,
            "Hard (1-200)": 200
        }

        self.max_number = 100
        self.secret_number = None
        self.attempts = 0

        # self.setup_ui()  # Removed because setup_ui is not defined
        self.difficulty_var = tk.StringVar(self.root)
        self.difficulty_var.set("Medium (1-100)")
        tk.OptionMenu(self.root, self.difficulty_var, *self.difficulty_levels.keys(), command=self.set_difficulty).pack(pady=5)

        self.instruction = tk.Label(self.root, text="Guess the number:", font=("Times New Roman", 14),bg="#f24329",fg="black")
        self.instruction.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Times New Roman", 14))
        self.entry.pack(pady=5)

        submit_img = Image.open(r"C:\Users\sujaa\Downloads\1000071974(1).png").resize((115, 40), Image.LANCZOS)
        submit_icon = ImageTk.PhotoImage(submit_img)
        self.submit_button = tk.Button(
            self.root,
            image=submit_icon,
            command=self.check_guess,
            borderwidth=0,
            bg="#f24329",
            activebackground="#f24329",
            width=115,
            height=40
        )
        self.submit_button.image = submit_icon  # Keep a reference
        self.submit_button.pack(pady=10)

        self.feedback = tk.Label(self.root, text="", font=("Times New Roman", 12),bg="#f24329" ,fg="blue")
        self.feedback.config(text="Enter your guess and click Submit.")
        self.feedback.pack(pady=5)

        restart_img = Image.open(r"C:\Users\sujaa\Downloads\1000071975(1).png").resize((115, 40), Image.LANCZOS)
        restart_icon = ImageTk.PhotoImage(restart_img)
        self.restart_button = tk.Button(
            self.root,
            image=restart_icon,
            command=self.reset_game,
            bg="#f24329",
            activebackground="#f24329",
            borderwidth=0,
            width=115,
            height=40
        )
        self.restart_button.image = restart_icon
        self.restart_button.pack(pady=10)

        self.set_difficulty(self.difficulty_var.get())

    def set_difficulty(self, level):
        self.max_number = self.difficulty_levels[level]
        self.reset_game()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback.config(text="Too low! Try again.", fg="blue")
            elif guess > self.secret_number:
                self.feedback.config(text="Too high! Try again.", fg="orange")
            else:
                messagebox.showinfo("🎉 Winner!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")
        self.instruction.config(text=f"Guess the number (1-{self.max_number}):")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()