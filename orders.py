import PySimpleGUI as sg
from screeninfo import get_monitors

from order_add import orders_add


def orders():
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Заказы", justification='center', font=font_title, size=(monitor.width, 5),
                 pad=((0, 0), (50, 0)))],
        [sg.Text("Дата регистрации / Дата выполнения заказы / Статус заказа", font=font_button), sg.Button("Добавить", font=font_button)],
        [], # список заказов
        [sg.Button("Назад", font=font_button)]
    ]

    layout[2].append(sg.Listbox(["10.01.2024 / 01.02.2024 / Выполнен"], font=font_button, background_color='green', size=(monitor.width, 10)))

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)
    window.finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        if event == "Добавить":
            window.Hide()
            orders_add()
            window.UnHide()
        elif event == "Назад":
            window.close()
            return