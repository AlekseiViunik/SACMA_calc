import tkinter as tk


class BlockEditor:
    def __init__(self, parent, block_button):
        """Creates a window for editing the block name."""

        # Save the button object to change the text later
        self.block_button = block_button

        # Create a Toplevel window
        self.window = tk.Toplevel(parent)
        self.window.title("Modifica Blocco")
        self.window.geometry("300x150")
        
        # Make the window modal (block interaction with the main window)
        self.window.grab_set()

        # Field for entering the block name
        tk.Label(
            self.window,
            text="Nome del blocco:",
            font=("Arial", 12)
        ).pack(pady=10)
        self.name_entry = tk.Entry(self.window, font=("Arial", 12))
        self.name_entry.pack(pady=5)
        self.name_entry.focus()

        # Buttons OK and Cancel
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        ok_button = tk.Button(
            button_frame,
            text="OK",
            width=10,
            command=self.save_block_name
        )
        ok_button.pack(side=tk.LEFT, padx=5)

        cancel_button = tk.Button(
            button_frame,
            text="Annulla",
            width=10,
            command=self.window.destroy
        )
        cancel_button.pack(side=tk.LEFT, padx=5)

    def save_block_name(self):
        """Saves the entered block name and closes the window."""
        new_name = self.name_entry.get().strip()
        if new_name:
            # Change the button text
            self.block_button.config(text=new_name)
        self.window.destroy()