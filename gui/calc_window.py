import tkinter as tk
from datetime import datetime
from gui.window_abstract import Window


class Calc(Window):
    def __init__(self, root):
        super().__init__(root, "Calcolare prezzi e materiali", "700x700")
        self.setup_ui()

    def setup_ui(self):
        # Основная форма с полями для ввода
        form_frame = tk.Frame(self.root)
        form_frame.pack(padx=20, pady=10, fill=tk.X)

        # Поля ввода (Cliente, Indirizzo, Data, Ingegnere, Numero foglio)
        self.create_label_entry(form_frame, "Cliente:", 0)
        self.create_label_entry(form_frame, "Indirizzo:", 1)
        self.create_label_entry(
            form_frame,
            "Data:",
            2,
            default=datetime.today().strftime('%d-%m-%Y')
        )
        self.create_label_entry(form_frame, "Ingegnere:", 3)
        self.create_label_entry(
            form_frame,
            "Numero foglio:",
            4,
            entry_type='number'
        )

        # Кнопка "Aggiungi Blocco" над прокручиваемым фреймом
        add_block_button = tk.Button(
            self.root,
            text="Aggiungi Blocco",
            command=self.add_block
        )
        add_block_button.pack(padx=20, pady=(10, 0), anchor="w")

        # Прокручиваемый фрейм
        scroll_container = tk.Frame(self.root, bd=2, relief="solid")
        scroll_container.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(scroll_container)
        scrollbar = tk.Scrollbar(
            scroll_container,
            orient="vertical",
            command=canvas.yview
        )
        self.inner_frame = tk.Frame(canvas)

        # Привязываем прокрутку
        self.inner_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        self.canvas_window = canvas.create_window(
            (0, 0),
            window=self.inner_frame,
            anchor="nw"
        )
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Счётчик блоков
        self.block_count = 0

        # Нижние кнопки управления
        bottom_buttons_frame = tk.Frame(self.root)
        bottom_buttons_frame.pack(padx=20, pady=10, fill=tk.X)

        buttons = [
            "Nuovo calcolo",
            "Caricare",
            "Salva come",
            "Salva",
            "Calcolare"
        ]
        for btn_text in buttons:
            tk.Button(
                bottom_buttons_frame,
                text=btn_text,
                width=15
            ).pack(side=tk.LEFT, padx=5)

    def create_label_entry(
        self,
        parent,
        label_text,
        row,
        default="",
        entry_type='text'
    ):
        """Создание лейблов и полей ввода."""
        label = tk.Label(parent, text=label_text, font=("Arial", 12))
        label.grid(row=row, column=0, sticky="w", pady=5)

        if entry_type == 'number':
            entry = tk.Entry(
                parent,
                font=("Arial", 12),
                validate="key",
                validatecommand=(
                    self.root.register(self.validate_number),
                    '%P'
                )
            )
        else:
            entry = tk.Entry(parent, font=("Arial", 12))

        entry.insert(0, default)
        entry.grid(row=row, column=1, sticky="ew", pady=5, padx=10)
        parent.grid_columnconfigure(1, weight=1)

    def validate_number(self, value):
        """Проверка, что введено только число."""
        return value.isdigit() or value == ""

    def add_block(self):
        """Добавляет новый блок с кнопками 'Blocco' и 'Cancellare' в
        прокручиваемом фрейме."""

        self.block_count += 1

        # Фрейм для группы кнопок (Blocco + Cancellare)
        block_frame = tk.Frame(self.inner_frame)
        block_frame.pack(fill=tk.X, padx=10, pady=5)

        # Кнопка 'Blocco'
        block_button = tk.Button(
            block_frame,
            text=f"Blocco {self.block_count}",
            width=30
        )
        block_button.pack(side=tk.LEFT, padx=5)

        # Кнопка 'Cancellare' с функцией удаления родительского фрейма
        delete_button = tk.Button(
            block_frame,
            text="Cancellare",
            width=10,
            command=lambda: self.delete_block(block_frame)
        )
        delete_button.pack(side=tk.LEFT, padx=5)

    def delete_block(self, block_frame):
        """Удаляет выбранный блок (кнопки 'Blocco' и 'Cancellare')."""
        block_frame.destroy()
