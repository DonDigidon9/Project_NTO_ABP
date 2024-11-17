import PySimpleGUI as sg
from screeninfo import get_monitors

def timber_products(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Виды лесопродукции", justification='center', font=font_title, size=(monitor.width, 2),
                 pad=((0, 0), (50, 0)))],
        # [sg.Canvas(background_color='purple', size=(int(9*monitor.width/10), int(8*monitor.height/10)), pad=((50, 0), (0, 0)))],
        [sg.Button("Добавить", font=font_button, border_width=5)],
        [], # для списка лесопродукции
        [sg.Button("Назад", font=font_button, pad=((0, 0), (0, 10)), border_width=5)]
    ]

    # TODO: заполнение всей лесопродукцией из БД
    layout[2].append(sg.Listbox(["Рейки"], size=(monitor.width, 10), font=font_button))

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)
    window.finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)
        if event == "Добавить":
            print()
            # TODO: сделать возможность добавления или убрать функционал
        elif event == "Назад":
            window.close()
            return