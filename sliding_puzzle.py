import tkinter as tk
from tkinter import messagebox
import random

class SlidingPuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("15-Puzzle Game")
        self.root.geometry("400x400")
        self.tiles = []
        self.empty_row, self.empty_col = 3, 3  # Empty tile position
        self.moves = 0

        # Initialize the puzzle board
        self.board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        self.shuffle_board()

        # Create the puzzle grid
        for i in range(4):
            row = []
            for j in range(4):
                tile = tk.Button(
                    root,
                    text=str(self.board[i][j]) if self.board[i][j] != 0 else "",
                    font=("Arial", 18),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.move_tile(i, j),
                )
                tile.grid(row=i, column=j, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)

        # Move counter label
        self.move_label = tk.Label(root, text=f"Moves: {self.moves}", font=("Arial", 14))
        self.move_label.grid(row=4, column=0, columnspan=4, pady=10)

        # Reset button
        reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        reset_button.grid(row=5, column=0, columnspan=4, pady=10)

    def shuffle_board(self):
        # Shuffle the board to create a solvable puzzle
        for _ in range(1000):
            neighbors = self.get_neighbors(self.empty_row, self.empty_col)
            move = random.choice(neighbors)
            self.swap_tiles(self.empty_row, self.empty_col, move[0], move[1])
            self.empty_row, self.empty_col = move[0], move[1]

    def get_neighbors(self, row, col):
        # Get valid neighboring tiles
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < 3:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < 3:
            neighbors.append((row, col + 1))
        return neighbors

    def swap_tiles(self, row1, col1, row2, col2):
        # Swap two tiles on the board
        self.board[row1][col1], self.board[row2][col2] = self.board[row2][col2], self.board[row1][col1]

    def move_tile(self, row, col):
        # Move a tile into the empty space
        if (abs(row - self.empty_row) + abs(col - self.empty_col)) == 1:
            self.swap_tiles(row, col, self.empty_row, self.empty_col)
            self.tiles[row][col].config(text="")
            self.tiles[self.empty_row][self.empty_col].config(text=str(self.board[self.empty_row][self.empty_col]))
            self.empty_row, self.empty_col = row, col
            self.moves += 1
            self.move_label.config(text=f"Moves: {self.moves}")
            if self.check_win():
                messagebox.showinfo("Congratulations!", f"You solved the puzzle in {self.moves} moves!")
                self.reset_game()

    def check_win(self):
        # Check if the puzzle is solved
        win_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        return self.board == win_board

    def reset_game(self):
        # Reset the game
        self.moves = 0
        self.move_label.config(text=f"Moves: {self.moves}")
        self.shuffle_board()
        for i in range(4):
            for j in range(4):
                self.tiles[i][j].config(text=str(self.board[i][j]) if self.board[i][j] != 0 else "")

if __name__ == "__main__":
    root = tk.Tk()
    game = SlidingPuzzle(root)
    root.mainloop()