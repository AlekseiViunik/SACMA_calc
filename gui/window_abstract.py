from abc import ABC, abstractmethod


class WindowAbstract(ABC):
    """Абстрактный класс для всех окон."""
    def __init__(self, root):
        self.root = root

    @abstractmethod
    def setup_ui(self):
        """Метод для создания UI. Должен быть реализован в дочернем классе."""
        pass


class Window(WindowAbstract):
    """Базовый класс для окон с общим функционалом."""
    def __init__(self, root, title, size):
        super().__init__(root)
        self.root.title(title)
        self.center_window(size)

    def center_window(self, size):
        """Центрирует окно относительно экрана."""
        self.root.geometry(size)
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width, window_height = map(int, size.split('x'))
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
