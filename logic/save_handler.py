import json
import os
from pathlib import Path
from tkinter import filedialog


class SaveHandler:
    def __init__(self):
        # Папка для сохранений
        self.save_dir = Path(__file__).resolve().parent.parent / "saves"
        self.save_dir.mkdir(exist_ok=True)

        # Путь к временному файлу
        self.temp_save_path = self.save_dir / "temp_save.json"

        # Инициализация временного файла при запуске
        self.initialize_temp_save()

    def initialize_temp_save(self):
        """Создаёт temp_save.json с пустыми значениями при открытии окна."""
        if not self.temp_save_path.exists():
            initial_data = {
                "client": "",
                "address": "",
                "date": "",
                "ingeneer": "",
                "sheetNo": 0,
                "blocks": []
            }
            self._write_to_file(initial_data)

    def _write_to_file(self, data):
        """Записывает данные в temp_save.json."""
        with open(self.temp_save_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def _read_from_file(self):
        """Читает данные из temp_save.json."""
        with open(self.temp_save_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def update_field(self, field, value):
        """Обновляет значение конкретного поля в temp_save.json."""
        data = self._read_from_file()
        data[field] = value
        self._write_to_file(data)

    def add_block(self, block_name):
        """Добавляет новый блок в temp_save.json."""
        data = self._read_from_file()
        data["blocks"].append({
            "name": block_name,
            "sections": []  # Зарезервировано для будущих секций
        })
        self._write_to_file(data)

    def save_as(self):
        """Открывает диалоговое окно для сохранения файла с новым именем."""
        file_path = filedialog.asksaveasfilename(
            initialdir=self.save_dir,
            title="Salva come",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            data = self._read_from_file()
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_temp_save(self):
        """Удаляет временный файл temp_save.json при закрытии окна."""
        if self.temp_save_path.exists():
            os.remove(self.temp_save_path)