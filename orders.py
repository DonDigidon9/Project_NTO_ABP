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

    def get_color_by_status(status):
        if status == "Черновик":
            return "white"
        elif status == "Согласован клиентом":
            return "orange"
        elif status == "Принят в производство":
            return "yellow"
        elif status == "Выполнен":
            return "green"
        else:
            return "white"  # По умолчанию

    orders = [
    "10.01.2024 / 01.02.2024 / Черновик",
    "15.01.2024 / 10.02.2024 / Согласован клиентом",
    "20.01.2024 / 15.02.2024 / Принят в производство",
    "25.01.2024 / 20.02.2024 / Выполнен"
    ]
    listbox_elements = []
    for i, order in enumerate(orders):
        status = order.split("/")[-1].strip()  # Последнее слово после "/"
        color = get_color_by_status(status)
        listbox_elements.append(
            [sg.Button(order, button_color=("black", color), font=('New Roman', 10), size=(150, 2), key=f"-ORDER-{i}-", pad=(0, 0))]
        )


    layout = [
        [sg.Text("Заказы", justification='center', font=font_title, size=(monitor.width, 5),
                 pad=((0, 0), (50, 0)))],
        [sg.Text("Дата регистрации / Дата выполнения заказы / Статус заказа", font=font_button), sg.Button("Добавить", font=font_button)],
        [sg.Column(listbox_elements, scrollable=True, size=(monitor.width, 500), vertical_scroll_only=True, key="-LISTBOX-")],
        [sg.Button("Назад", font=font_button)]
    ]

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