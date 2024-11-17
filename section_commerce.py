import PySimpleGUI as sg
from screeninfo import get_monitors

from customers import customers
from orders import orders
from timber_products import timber_products

def section_commerce(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Выберите раздел", justification='center', font=font_title, size=(monitor.width, 5),
                 pad=((0, 0), (50, 0)))],
        [sg.Push(), sg.Button("Клиенты", size=size_button, font=font_button),
         sg.Button("Виды лесопродукции", size=size_button, font=font_button),
         sg.Button("Заказы", size=size_button, font=font_button), sg.Push()],
        [sg.Push()],
        [sg.Button("Назад", font=font_button), sg.Push()]
    ]

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)
    window.finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)
        if event == "Клиенты":
            window.Hide()
            customers(app)
            window.UnHide()
        elif event == "Виды лесопродукции":
            window.Hide()
            timber_products(app)
            window.UnHide()
        elif event == "Заказы":
            window.Hide()
            orders(app)
            window.UnHide()
        elif event == "Назад":
            window.close()
            return