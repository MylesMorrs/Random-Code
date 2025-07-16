import tkinter as tk
import socket
import threading

SERVER_IP = '127.0.0.1'  # Replace with server's IP
PORT = 9999

class RPSGameClient:
    def __init__(self, master):
        self.master = master
        master.title("RPS Client")
        self.choices = ["Rock", "Paper", "Scissors"]
        self.choice = None
        self.opponent_choice = None
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread(target=self.connect_server, daemon=True).start()

        self.label = tk.Label(master, text="Connecting to server...")
        self.label.pack(pady=10)

        self.buttons = []
        for c in self.choices:
            btn = tk.Button(master, text=c, command=lambda choice=c: self.send_choice(choice), state=tk.DISABLED)
            btn.pack()
            self.buttons.append(btn)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=20)

    def connect_server(self):
        self.s.connect((SERVER_IP, PORT))
        self.label.config(text="Connected to server! Choose your move:")
        for btn in self.buttons:
            btn.config(state=tk.NORMAL)
        threading.Thread(target=self.receive_choice, daemon=True).start()

    def send_choice(self, choice):
        self.choice = choice
        self.s.sendall(choice.encode())
        self.label.config(text=f"You chose: {choice}. Waiting for opponent...")
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def receive_choice(self):
        while True:
            data = self.s.recv(1024)
            if not data:
                break
            self.opponent_choice = data.decode()
            self.show_result()

    def show_result(self):
        result = self.get_winner(self.opponent_choice, self.choice)
        self.result_label.config(text=f"Opponent chose: {self.opponent_choice}\n{result}")
        for btn in self.buttons:
            btn.config(state=tk.NORMAL)
        self.label.config(text="Choose your move:")

    def get_winner(self, p1, p2):
        if p1 == p2:
            return "It's a Tie!"
        elif (p1 == "Rock" and p2 == "Scissors") or (p1 == "Paper" and p2 == "Rock") or (p1 == "Scissors" and p2 == "Paper"):
            return "You Win!"
        else:
            return "You Lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGameClient(root)
    root.mainloop()
