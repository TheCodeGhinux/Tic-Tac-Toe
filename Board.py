import tkinter as tk
from tkinter import font


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac_Toe Game")
        self._cells = {}

    def board(self):
        frame = tk.Frame(master=self)
        frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )

        self.display.pack()
