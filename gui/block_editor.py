import tkinter as tk


class BlockEditor:
    def __init__(self, parent, block_button):
        """Creates a window for editing the block name."""

        # Save the button object to change the text later
        self.block_button = block_button

        self.section_count = 0

        # Create a Toplevel window
        self.window = tk.Toplevel(parent)
        self.window.title("Modifica Blocco")
        self.window.geometry("420x500")
        
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

        # Кнопка "Aggiungi Sezione" перед прокручиваемым фреймом
        add_section_button = tk.Button(self.window, text="Aggiungi Sezione", command=self.add_section)
        add_section_button.pack(pady=(20, 5), anchor="w", padx=10)

        # Прокручиваемый фрейм для секций
        scroll_container = tk.Frame(self.window, bd=2, relief="solid")
        scroll_container.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(scroll_container)
        scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
        self.inner_frame = tk.Frame(canvas)

        # Привязываем прокрутку
        self.inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        self.canvas_window = canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

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

    def add_section(self):
        """Добавляет новую секцию с кнопками 'Sezione N' и 'Cancellare'."""
        self.section_count += 1

        # Фрейм для кнопок секции
        section_frame = tk.Frame(self.inner_frame)
        section_frame.pack(fill=tk.X, padx=10, pady=5)

        # Кнопка 'Sezione N'
        section_button = tk.Button(section_frame, text=f"Sezione {self.section_count}", width=30)
        section_button.pack(side=tk.LEFT, padx=5)

        # Кнопка 'Cancellare' для удаления секции
        delete_button = tk.Button(section_frame, text="Cancellare", width=10, 
                                  command=lambda: self.delete_section(section_frame))
        delete_button.pack(side=tk.LEFT, padx=5)

    def delete_section(self, section_frame):
        """Удаляет выбранную секцию."""
        section_frame.destroy()
