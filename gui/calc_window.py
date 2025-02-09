import tkinter as tk

from pathlib import Path

from gui.window_abstract import Window


class Calc(Window):
    def __init__(self, root):
        super().__init__(root, "Calcolare prezzi e materiali", "1000x700")
        self.setup_ui()

    def setup_ui(self):
        # Image frame
        img_frame = tk.Frame(self.root, bg="blue", height=300)
        img_frame.pack(fill=tk.X, padx=20, pady=10)

        base_dir = Path(__file__).resolve().parent.parent
        img_path = base_dir / "images" / "nscaffali.png"
        image = tk.PhotoImage(file=img_path)
        image = image.subsample(1, 1)
        label = tk.Label(img_frame)
        label.image = image
        label['image'] = label.image
        label.place(relx=0.5, rely=0.5, anchor='center')

        # Checkbox frame (place vertically)
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(fill=tk.X, padx=20, pady=5, anchor="w")

        # Checkbox Sismoresistenza (Text is on the left,
        # checkbox is on the right)
        self.sismo_var = tk.BooleanVar()
        sismo_frame = tk.Frame(controls_frame)
        sismo_frame.pack(anchor="w", pady=2)
        tk.Label(sismo_frame, text="Sismoresistenza").pack(side=tk.LEFT)
        sismo_check = tk.Checkbutton(sismo_frame, variable=self.sismo_var)
        sismo_check.pack(side=tk.LEFT)

        # N scaffali label + entry field (under the checkbox)
        scaffali_frame = tk.Frame(controls_frame)
        scaffali_frame.pack(anchor="w", pady=2)
        tk.Label(scaffali_frame, text="N scaffali:").pack(side=tk.LEFT)
        self.scaffali_entry = tk.Entry(scaffali_frame, width=5)
        self.scaffali_entry.pack(side=tk.LEFT)

        # Button "Applica"
        apply_button = tk.Button(
            scaffali_frame,
            text="Applica",
            command=self.create_scaffali_frames
        )
        apply_button.pack(side=tk.LEFT, padx=5)

        # Scrolling frame (bg green)
        scroll_container = tk.Frame(self.root, bg="green")
        scroll_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        canvas = tk.Canvas(scroll_container, bg="green")
        scrollbar = tk.Scrollbar(
            scroll_container,
            orient="vertical",
            command=canvas.yview
        )
        self.inner_frame = tk.Frame(canvas, bg="green")

        # Adjust inner frame width when canvas width is changed
        def resize_inner_frame(event):
            canvas_width = event.width
            canvas.itemconfig(self.canvas_window, width=canvas_width)

        def update_scrollregion(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        self.canvas_window = canvas.create_window(
            (0, 0),
            window=self.inner_frame,
            anchor="nw"
        )
        canvas.bind("<Configure>", resize_inner_frame)
        self.inner_frame.bind("<Configure>", update_scrollregion)

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_scaffali_frames(self):
        # Destroy old frames
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        try:
            n_scaffali = int(self.scaffali_entry.get())
        except ValueError:
            print("Enter the correct number")
            return

        self.inner_frame.update_idletasks()
        frame_width = self.inner_frame.winfo_width()
        print(f"Ширина контейнера: {frame_width}")

        for i in range(n_scaffali):
            yellow_frame = tk.Frame(
                self.inner_frame,
                bg="yellow",
                height=200, width=frame_width
            )
            yellow_frame.pack(fill=tk.BOTH, pady=20, padx=0)

            # Fix height so that it doesn't shrink
            yellow_frame.pack_propagate(False)

            tk.Label(
                yellow_frame,
                text=f"Scaffale {i+1}",
                bg="yellow"
            ).pack(padx=5, pady=5)
