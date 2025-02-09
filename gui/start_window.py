from tkinter import ttk
import tkinter as tk
from constants import const as c
from gui.window_abstract import Window
from gui.calc_window import Calc


class App(Window):
    def __init__(self, root):
        super().__init__(root, c.APP_TITLE, c.START_WINDOW_SIZE)
        self.setup_ui()

    def setup_ui(self):
        welcome_label = tk.Label(
            self.root, text=c.WELCOME_TEXT,
            font=("Arial", 20), fg="blue"
        )
        welcome_label.pack(pady=10)

        name_label = tk.Label(self.root, text=c.LABEL_NAME, font=("Arial", 12))
        name_label.pack()
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        dropdown_label = tk.Label(
            self.root,
            text=c.DROPDOWN_LABEL,
            font=("Arial", 12)
        )
        dropdown_label.pack()
        self.action_var = tk.StringVar(value=c.ACTION_CALCULATE)
        actions_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.action_var,
            font=("Arial", 12),
            state="readonly"
        )
        actions_dropdown['values'] = [c.ACTION_CALCULATE]
        actions_dropdown.pack(pady=5)

        avanti_button = tk.Button(
            self.root, text=c.BUTTON_TEXT,
            font=("Arial", 12), command=self.next_window
        )
        avanti_button.pack(pady=20)

    def next_window(self):
        selected_action = self.action_var.get()
        self.root.destroy()  # Закрыть текущее окно
        if selected_action == c.ACTION_CALCULATE:
            new_root = tk.Tk()
            Calc(new_root)  # Открытие окна Calc
            new_root.mainloop()
