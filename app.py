import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("300x300")
        self.current_player = "X"
        self.board = [""] * 9  # Represents the 3x3 board
        self.buttons = []  # To hold the button widgets

        # Create the game board
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    root,
                    text="",
                    font=("Arial", 20),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.on_click(i, j),
                )
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(button)

        # Reset button
        reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_click(self, row, col):
        index = 3 * row + col
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != "":
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()