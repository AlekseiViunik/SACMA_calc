import tkinter as tk
from tkinter import ttk
from constants import const as c


class App:
    def __init__(self, root):
        self.root = root
        self.root.title(c.APP_TITLE)
        self.center_window(c.START_WINDOW_SIZE)

        # welcome label
        welcome_label = tk.Label(
            root, text=c.WELCOME_TEXT,
            font=("Arial", 20), fg="blue"
        )
        welcome_label.pack(pady=10)

        # Enter name field
        name_label = tk.Label(root, text=c.LABEL_NAME, font=("Arial", 12))
        name_label.pack()
        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        # Dropdown list
        dropdown_label = tk.Label(
            root,
            text=c.DROPDOWN_LABEL,
            font=("Arial", 12)
        )
        dropdown_label.pack()
        self.action_var = tk.StringVar(value=c.ACTION_CALCULATE)
        actions_dropdown = ttk.Combobox(
            root,
            textvariable=self.action_var,
            font=("Arial", 12),
            state="readonly"
        )
        actions_dropdown['values'] = [c.ACTION_CALCULATE]
        actions_dropdown.pack(pady=5)

        # Go button
        go_button = tk.Button(
            root, text=c.BUTTON_TEXT,
            font=("Arial", 12), command=self.next_window
        )
        go_button.pack(pady=20)

    def center_window(self, size):
        """Centers window on the screen."""
        self.root.geometry(size)
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width, window_height = map(int, size.split('x'))
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def next_window(self):
        """Closes current window and opens the new one."""
        selected_action = self.action_var.get()
        print(f"Action selected: {selected_action}")

        self.root.destroy()

        if selected_action == c.ACTION_CALCULATE:
            open_calculation_window()


def open_calculation_window():
    """Пример открытия нового окна."""
    new_root = tk.Tk()
    new_root.title("Calcolare prezzi e materiali")
    new_root.geometry("400x300")
    label = tk.Label(
        new_root, text="Окно расчета!", font=("Arial", 16)
    )
    label.pack(pady=50)
    new_root.mainloop()
