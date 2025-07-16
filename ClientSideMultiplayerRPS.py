import socket
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog

class RPSClient:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.label = tk.Label(master, text="Waiting for server message...", width=40)
        self.label.pack(pady=10)

        self.rock_button = tk.Button(master, text="Rock", width=12, command=lambda: self.send_move("rock"))
        self.paper_button = tk.Button(master, text="Paper", width=12, command=lambda: self.send_move("paper"))
        self.scissors_button = tk.Button(master, text="Scissors", width=12, command=lambda: self.send_move("scissors"))

        self.rock_button.pack(pady=2)
        self.paper_button.pack(pady=2)
        self.scissors_button.pack(pady=2)

        self.sock = None
        self.input_thread = threading.Thread(target=self.receive_messages, daemon=True)
        self.connect_to_server()

    def connect_to_server(self):
        server_ip = simpledialog.askstring("Server IP", "Enter server IP address:", parent=self.master)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((server_ip, 12345))
            self.input_thread.start()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect: {e}")
            self.master.destroy()

    def send_move(self, move):
        try:
            self.sock.send(move.encode())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send move: {e}")
            self.master.destroy()

    def receive_messages(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode()
                self.update_label(msg)
            except Exception:
                break

    def update_label(self, text):
        def update():
            self.label.config(text=text)
        self.master.after(0, update)

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSClient(root)
    root.mainloop()
