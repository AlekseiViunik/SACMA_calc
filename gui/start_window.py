import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SACMA calc")
        self.root.geometry("1024x768")

        # Добавим простой виджет для проверки
        label = tk.Label(
            root, text="Добро пожаловать в приложение!",
            font=("Arial", 16)
        )
        label.pack(pady=20)
