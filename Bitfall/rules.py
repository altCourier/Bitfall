"""
rules.py
This module shows the user the rules for the game.
"""

import tkinter as tk
from menu import Menu

class Rules(Menu):
    def __init__(self):
        tk.Tk.__init__(self)
        self.main_window()
        self.show_rules()

    def show_rules(self):
        rules_text: str = """
        Welcome to Bitfall.

        1. Objective:
           Gain as many points as you can before time runs out.

        2. Modes:
           - Binary: Convert binary to decimal.
           - Hexadecimal: Convert hexadecimal to decimal.

        3. Scoring:
           - Correct answers = Points.
           - Bonus for streaks.

        Good luck and have fun!
        """
        # Rules Label
        rules_label = tk.Label(self, text = rules_text, justify = "left", font = ("Ariel", 12), wraplength = 550)
        rules_label.pack()

        # Back Button
        self.go_back = tk.Button(self, text = "I got it!", font = ("Ariel", 12), command = self.go_back)
        self.go_back.pack()

    def go_back(self):
        self.destroy()
        menu = Menu()
        menu.mainloop()

if __name__ == "__main__":
    rules = Rules()
    rules.mainloop()