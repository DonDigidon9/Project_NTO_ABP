import json
import os
import sys

from service import service
from LogicClasses.App import App

# Определение базового пути
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):  # Проверка существования _MEIPASS
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Если файл находится в ".venv"
json_path = os.path.join(base_path, '.venv', 'file.json')

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
