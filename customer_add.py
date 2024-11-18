import json
from dataclasses import asdict

import PySimpleGUI as sg
from screeninfo import get_monitors

from LogicClasses.App import App
from LogicClasses.Customer import Customer

def customers_add(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Добавить клиента(заказчика)", justification='center', font=font_title, size=(monitor.width, 3),
                 pad=((0, 0), (20, 0)))],
        [sg.Text("Название организации:", font=font_button), sg.InputText(key='-ORGANIZATION-', font=font_button, size=(monitor.width, 1))],
        [sg.Push()],
        [sg.Text('', size=(monitor.width, 4))],
        [sg.Button("Сохранить", font=font_button)],
        [sg.Button("Назад", font=font_button)]
    ]

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        if event == "Сохранить":
            new_customer = Customer(organization=values['-ORGANIZATION-'])
            app.customers_.append(new_customer)
            json_data = json.dumps(asdict(app), indent=4)
            with open("file.json", "w") as file:
                file.write(json_data)
            window.close()
            return App(**json.loads(json_data))
        elif event == "Назад":
            window.close()
            return app