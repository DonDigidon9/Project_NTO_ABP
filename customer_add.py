import json
import os
import sys
from dataclasses import asdict
import PySimpleGUI as sg
from screeninfo import get_monitors
from LogicClasses.App import App
from LogicClasses.Customer import Customer
from order_add import open_window_fail

# Определяем путь к базовой папке
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Получение пути к JSON файлу
def get_json_path():
    return os.path.join(base_path, '.venv', 'file.json')

# Чтение JSON
def load_from_json():
    json_path = get_json_path()
    if not os.path.exists(json_path):
        with open(json_path, "w") as file:
            file.write("{}")
    try:
        with open(json_path, "r") as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        sg.popup_error(f"Ошибка чтения JSON: {e}")
        return {}

# Запись JSON
def save_to_json(app):
    try:
        with open(get_json_path(), "w") as file:
            json_data = json.dumps(asdict(app), indent=4)
            file.write(json_data)
    except IOError as e:
        sg.popup_error(f"Ошибка записи JSON: {e}")

# Добавление клиента
def customers_add(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)
    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Добавить клиента(заказчика)", justification='center', font=font_title, size=(monitor.width, 3),
                 pad=((0, 0), (20, 0)))],
        [sg.Text("Название организации:", font=font_button),
         sg.InputText(key='-ORGANIZATION-', font=font_button, size=(monitor.width, 1))],
        [sg.Push()],
        [sg.Text('', size=(monitor.width, 4))],
        [sg.Button("Сохранить", font=font_button), sg.Button("Назад", font=font_button)]
    ]

    size_layout = (monitor.width, monitor.height - 1)
    window = sg.Window(title, layout, size=size_layout, resizable=False, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Назад"):
            window.close()
            return app

        if event == "Сохранить":
            if len(values['-ORGANIZATION-']) == 0:
                open_window_fail("Введите название")
                continue
            app.add_customer(values['-ORGANIZATION-'])
            save_to_json(app)
            window.close()
            return app
