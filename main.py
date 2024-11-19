import json
import os
import sys

from service import service
from LogicClasses.App import App

# Определение базового пути
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):  # Проверка на скомпилированное приложение
    base_path = sys._MEIPASS  # Путь к временной папке, куда PyInstaller распаковывает файлы
else:
    base_path = os.path.dirname(__file__)  # Путь к текущему скрипту в режиме разработки

# Если в режиме разработки, путь к файлу должен быть в .venv
if not getattr(sys, 'frozen', False):  # Только в режиме разработки
    json_path = os.path.join(base_path, '.venv', 'file.json')  # Путь к файлу в .venv
else:
    json_path = os.path.join(base_path, 'file.json')  # В скомпилированном приложении, файл должен быть в корне

# Проверка существования файла
if not os.path.exists(json_path):
    raise FileNotFoundError(f"Не удалось найти файл: {json_path}")

# Загрузка данных из JSON
with open(json_path, 'r') as file:
    json_text = file.read()
    data = json.loads(json_text)
    app = App(**data)

# Передача объекта App в сервис
service(app)
