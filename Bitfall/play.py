import tkinter as tk
from tkinter import messagebox
from menu import Menu
import random
import os

values = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', 
 '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 
 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

class Play(Menu):
    def __init__(self) -> None:
        """
        Initiate the playing

        """
        tk.Tk.__init__(self)
        self.main_window()

        # Choose mode for the playthrough.
        self.choose_mode()
    
    def choose_mode(self):
            """
            Choose the game mode.
            """

            # Frame to hold widgets
            self.mode_frame = tk.Frame(self)
            self.mode_frame.pack(fill = "both", expand =True)

            # Welcome Label
            self.welcome_label = tk.Label(self.mode_frame, text = "Before we begin,", font = "Courier")
            self.welcome_label.pack(pady = (80,0))

            # Choose Label
            self.choose_mode = tk.Label(self.mode_frame, text = "Choose your mode.", font = "Courier")
            self.choose_mode.pack(padx = 10, pady = 10)

            # Binary Button
            self.binary_button = tk.Button(self.mode_frame, text = "Binary", font = "Courier", command = lambda: self.start_game("binary"), width = 15)
            self.binary_button.pack(padx = 10, pady = 10)

            # Hexadecimal Button
            self.hex_button = tk.Button(self.mode_frame, text = "Hexadecimal", font = "Courier", command = lambda: self.start_game("hex"), width = 15)
            self.hex_button.pack(padx = 10, pady = 10)

            # Mishap Button
            self.mishap = tk.Button(self.mode_frame, text = "Oops, wrong button.", font = "Courier", command = self.go_back)
            self.mishap.pack(pady = 10)

    def start_game(self, mode):
        """
        Show the initial screen.
        """
        self.mode = mode

        # Forget all the widgets to use grid layout.
        self.clear_widgets()

        # Configure the layout
        self.grid_columnconfigure(0, weight = 3)
        self.grid_columnconfigure(1, weight = 1)

        for row in range(4):
            self.grid_rowconfigure(row, weight = 1)

        # Question Box
        self.question_var = tk.StringVar( value = "Convert this value")
        self.question_box = tk.Entry(self, font = ("Courier", 16), textvariable = self.question_var, state = "readonly")
        self.question_box.grid(row = 0, column = 0, sticky = "ew")
        
        # Entry Box for answer
        self.answer_entry = tk.Entry(self, font = ("Courier", 16))
        self.answer_entry.grid(row = 1, column = 0, sticky = "ew")

        # Start Button to start the game cycle
        self.start_button = tk.Button(self, text="Start", font = ("Courier", 16), command = self.start_game_cycle)
        self.start_button.grid(row = 3, column = 1, padx = 20, pady = 20)
        
        # Enter the value
        self.answer_check_button = tk.Button(self, text="Check", font = ("Courier", 16), command = self.check_answer)
        self.answer_check_button.grid(row = 2, padx = 20, pady = 20, column = 0)
        
        # Initialize the timer
        self.time_elapsed : int = 0
        self.timer_label = tk.Label(self, text = "00:00", font = ("Courier", 16), fg = "Black", anchor = "ne")
        self.timer_label.grid(row = 0, column = 1, padx = 20, pady = 20)

        # Scoreboard
        self.scoreboard_label = tk.Label(self, text = "Score", font = ("Courier", 16), fg = "Black", anchor = "e")
        self.scoreboard_label.grid(row = 1, column = 1)

        # Display score
        self.current_score = 0
        self.streak = 1
        self.score = tk.StringVar(value = str(self.current_score))
        self.scoreboard = tk.Entry(self, font = ("Courier", 16), textvariable = self.score, state = "readonly")
        self.scoreboard.grid(row = 2, column = 1, sticky = "e")

    def check_answer(self, event = None):
        """
        Check if self.answer_entry is correct with self.question_box
        """
        entered_answer = self.answer_entry.get().strip().upper()
        if entered_answer == self.correct_answer:
            print(f"Player has successed: {entered_answer}")
            self.current_score += 50 * self.streak
            self.streak += 1
            self.score.set(str(self.current_score))
            self.answer_entry.delete(0, tk.END)
            self.pick_value()
        else:
            print(f"Player has failed: {entered_answer}")
            self.answer_entry.delete(0, tk.END)
            self.streak = 1

    def start_game_cycle(self):
        """
        Start the game and the timer
        """
        self.start_button.grid_forget()  # Hide the start button once the game starts
        escape_early = tk.Button(self, text="Exit Early", font = ("Courier", 16), command = self.go_back)
        escape_early.grid(row = 3, column = 0, padx = 20, pady = 20)
        self.update_timer() # Start the timer
        self.pick_value() # Pick the first value

    def pick_value(self):
        """
        Pick a value based on the mode (binary or hex) and display it.
        """
        self.random_key = random.choice(list(values.keys()))

        if self.mode == "hex":
            self.question_var.set(values[self.random_key])
            self.correct_answer = self.random_key

        elif self.mode == "binary":
            self.correct_answer = values[self.random_key]
            self.question_var.set(self.random_key)

    def update_timer(self):
        """
        Keep track of timer and update timer
        """
        self.game_running = True
        if self.game_running and self.time_elapsed < 60:
            seconds = self.time_elapsed % 60
            self.timer_label.config(text = f"00:{seconds:02}")
            self.time_elapsed += 1
            self.after(1000, self.update_timer)
        elif self.time_elapsed == 60:
            self.timer_label.config(text = f"01:00")
            self.save_score_to_file
        else:
            self.timer_label.config(text = "Time's up!")
            self.game_running = False

    def save_score_to_file(self):
        """
        Save the current score to a file.
        """
        score_file = scores.txt

        if not os.path.exists(score_file):
            with open(score_file, "w") as file:
                file.write(f"Score: {self.current_score}\n")
            print("File created and score saved.")

        else:
            with open(score_file, "a") as file:
                file.write(f"Score: {self.current_score}\n")
            print("Score appended to file.")

    def clear_widgets(self):
        """
        Forget all packed widgets and reset layout to grid.
        """
        for widget in self.winfo_children():
            widget.pack_forget()

    # Go back to the main menu.
    def go_back(self):
        print("Going back to menu...")
        self.destroy()
        menu = Menu()
        menu.mainloop()