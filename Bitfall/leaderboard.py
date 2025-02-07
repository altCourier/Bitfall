import tkinter as tk
from menu import Menu
import os

class Leaderboard(Menu):
    def __init__(self):
        tk.Tk.__init__(self)
        self.main_window()
        
        if not os.path.exists("scores.txt"):
            # Label to show not existent
            tk.Label(self, text = "There is no existent file found.",  font=("Courier", 20)).grid(pady = 160, padx = 40)
        
        else:
            # Label for the leaderboard title   
            self.leaderboard_title = tk.Label(self, text="Leaderboard", font=("Courier", 24))
            self.leaderboard_title.pack(pady=10)

            # Create a listbox to display the leaderboard
            self.leaderboard_listbox = tk.Listbox(self, font=("Courier", 16), width=40, height=10)
            self.leaderboard_listbox.pack(pady=20)

            # Button to go back to the main menu
            self.back_button = tk.Button(self, text="Back to Menu", font=("Courier", 16), command=self.go_back)
            self.back_button.pack(pady=10)

            # Load the leaderboard data
            self.load_leaderboard()
    def load_leaderboard(self):
        """
        Load the leaderboard from the scores file and display it.
        """
        with open("scores.txt", 'r') as file:
                scores = []
                # Read lines to get the scores
                for line in file.readlines():
                    score = line.strip()
                    scores.append(int(score))
                # Sort the scores
                scores.sort(reverse = True)
                
                # Append to listbox
                for score in scores:
                    self.leaderboard_listbox.insert(tk.END, score)
    def go_back(self):
        """
        Close the leaderboard window and return to the main menu.
        """
        self.destroy()
        menu = Menu()
        menu.mainloop()
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.mainloop()