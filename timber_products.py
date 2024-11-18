import PySimpleGUI as sg
from screeninfo import get_monitors

def timber_products(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    # app.timber_products_ = [TimberProducts("Сырые пиломатериалы"), TimberProducts("Сухие пиломатериалы"), TimberProducts("Строгранные доски"), TimberProducts("Рейки"), TimberProducts("Брус"), TimberProducts("Пеллеты")]

    mas_timber_products = []
    for timber_product in app.timber_products_:
        mas_timber_products.append(timber_product['name'])

    layout = [
        [sg.Text("Виды лесопродукции", justification='center', font=font_title, size=(monitor.width, 2),
                 pad=((0, 0), (50, 0)))],
        [sg.Listbox(mas_timber_products, size=(monitor.width, 10), font=font_button)], # для списка лесопродукции
        [sg.Button("Назад", font=font_button, pad=((0, 0), (0, 10)), border_width=5)]
    ]

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)
    window.finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        elif event == "Назад":
            window.close()
            return app