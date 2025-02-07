"""
Run main.py in order to start the game.
"""
from menu import Menu

def open_menu():
    menu = Menu()
    menu.mainloop()

if __name__ == "__main__":
    open_menu()