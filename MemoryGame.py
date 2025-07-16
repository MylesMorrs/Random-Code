import tkinter as tk
import random

# Emoji pairs
symbols = list("🐶🐱🐭🐹🐰🦊🐻🐼") * 2
random.shuffle(symbols)
board = [symbols[i:i+4] for i in range(0, 16, 4)]
revealed = [[False]*4 for _ in range(4)]

# Track selected cards
selected = []

def on_click(x, y):
    global selected

    if revealed[x][y] or len(selected) == 2:
        return

    buttons[x][y].config(text=board[x][y])
    selected.append((x, y))

    if len(selected) == 2:
        root.after(500, check_match)

def check_match():
    global selected
    x1, y1 = selected[0]
    x2, y2 = selected[1]

    if board[x1][y1] == board[x2][y2]:
        revealed[x1][y1] = True
        revealed[x2][y2] = True
        buttons[x1][y1].config(bg="lightgreen")
        buttons[x2][y2].config(bg="lightgreen")
    else:
        buttons[x1][y1].config(text="❓")
        buttons[x2][y2].config(text="❓")

    selected = []

    if all(all(row) for row in revealed):
        win_label.config(text="You won! 🎉")

# Create GUI
root = tk.Tk()
root.title("Memory Match Game")

buttons = [[None]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text="❓", font=("Arial", 24), width=4, height=2,
                        command=lambda x=i, y=j: on_click(x, y))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

win_label = tk.Label(root, text="", font=("Arial", 18))
win_label.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
