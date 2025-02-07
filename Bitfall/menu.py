"""
menu.py
This module contains menu structure of the game.
"""

import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

class Menu(tk.Tk):
    def __init__(self):
        """
        Initialize the menu UI.

        """
        super().__init__()

        # Menu Area
        self.grid_rowconfigure(0, weight = 19)
        self.grid_columnconfigure(0, weight = 1)

        # Icons Area
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(1, weight = 0)

        # Create main window
        self.main_window()

        # Create the widgets
        self.create_menu_widgets()
        self.small_icons()


    def main_window(self):
        """
        self.main_window(self)

        Used for positioning the screen in the middle.
        """

        # Designing the window
        self.title("Bitfall")
        self.window_width = 600
        self.window_height = 400

        # Get screen sizes
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Positioning of the screen
        self.center_x = (self.screen_width // 2) - (self.window_width // 2)
        self.center_y = (self.screen_height // 2) - (self.window_height // 2)

        # Position the screen
        self.geometry(f"{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}")

        # Disable the resizability
        self.resizable(False, False)

    def create_menu_widgets(self):
        """
        Create and configure widgets for UI

        """ 

        # Menu Frame 
        self.menu_frame = tk.Frame(self)
        self.menu_frame.grid(row = 0, column = 0)

        # Menu Label
        self.welcome = tk.Label(self.menu_frame, text = "Bitfall", font = ("Courier", 24, "bold"))
        self.welcome.grid(row = 0, column = 0)

        # Play Button
        self.play_button = tk.Button(self.menu_frame, text = "Play", font = "Courier", command = self.play)
        self.play_button.grid(row = 1, column = 0, pady = 10)

        # Leaderboard Button
        self.leaderboard = tk.Button(self.menu_frame, text = "Leaderboard", font = "Courier", command = self.leaderboard)
        self.leaderboard.grid(row = 2, column = 0, pady = 10)

        # Rules Button
        self.rules = tk.Button(self.menu_frame, text = "Rules", font = "Courier", command = self.open_rules)
        self.rules.grid(row = 3, column = 0, pady = 10)

        # Exit Button
        self.leave_game = tk.Button(self.menu_frame, text = "Exit", font = "Courier", command = exit)
        self.leave_game.grid(row = 5, column = 0, pady = 10)

    def small_icons(self):
        """
        Create the small icons on the left corner.
        """
        # Icon Frame
        self.icons_frame = tk.Frame(self)
        self.icons_frame.grid(row = 1, column = 0, sticky = "sw", padx = 10, pady = 10)

        """
        Resizing the Logo image
        """
        logo_before = Image.open("assets/logo.png")
        original_width, original_height = logo_before.size
        ratio = original_width / original_height

        new_width: int = 20
        new_height = int(new_width / ratio)

        logo_before = logo_before.resize((new_width, new_height))
        self.logo_img = ImageTk.PhotoImage(logo_before)

        """
        Resizing the LinkedIn image
        """
        linked_before = Image.open("assets/linkedin.png")

        linked_og_width, linked_og_height = linked_before.size
        ratio = linked_og_width / linked_og_height

        linked_new_width: int = 22
        linked_new_height = int(linked_new_width / ratio)

        linked_before = linked_before.resize((linked_new_width, linked_new_height))
        self.linked_img = ImageTk.PhotoImage(linked_before)

        # Logo Button
        my_logo = tk.Button(self.icons_frame, image = self.logo_img, command = lambda: webbrowser.open("https://github.com/altCourier"))
        my_logo.grid(row = 0, column = 0)

        # Linked In Button
        self.linkedin = tk.Button(self.icons_frame, image = self.linked_img, command = lambda: webbrowser.open("https://www.linkedin.com/in/slauluyol/"))
        self.linkedin.grid(row = 0, column = 1, padx = 5)

    def play(self):
        """
        Initiate playthrough.
        """
        from play import Play
        self.destroy()
        play = Play()
        play.mainloop()

    def leaderboard(self):
        """
        Open the leaderboard window.
        """
        from leaderboard import Leaderboard
        self.destroy()
        leaderboard = Leaderboard()
        leaderboard.mainloop()

    def open_rules(self):
        """
        Open the rules window.
        """
        from rules import Rules
        self.destroy()
        rules = Rules()
        rules.mainloop()


if __name__ == "__main__":
    menu = Menu()
    menu.mainloop()