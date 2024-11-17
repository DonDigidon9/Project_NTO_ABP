import PySimpleGUI as sg
from screeninfo import get_monitors

from customer_add import customers_add


def customers(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Клиенты", justification='center', font=font_title, size=(monitor.width, 5),
                 pad=((0, 0), (50, 0)))],
        [sg.Text("Организация / ФИО / дата начала сотрудничества", font=font_button), sg.Button("Добавить", font=font_button)],
        [], # список клиентов
        [sg.Button("Назад", font=font_button)]
    ]

    # TODO: заполнение списка клиентов из БД
    layout[2].append(sg.Listbox(["Компания1 / Фамилия Имя Отчество 1 / Некая дата"], size=(monitor.width, 10), font=font_button))

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)
    window.finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        if event == "Добавить":
            window.Hide()
            customers_add(app)
            window.UnHide()
        elif event == "Назад":
            window.close()
            return