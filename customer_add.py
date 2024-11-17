import PySimpleGUI as sg
from screeninfo import get_monitors


def customers_add():
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Добавить клиента(заказчика)", justification='center', font=font_title, size=(monitor.width, 5),
                 pad=((0, 0), (50, 0)))],
        [sg.Text("Название организации:", font=font_button), sg.Input()],
        [sg.Text("ФИО клиента:", font=font_button), sg.Input()],
        [sg.Text("Дата:", font=font_button),
         sg.Input(),
         sg.CalendarButton("Календарь", close_when_date_chosen=True, format='%Y-%m-%d', default_date_m_d_y=(16,11,2024))], # TODO: сделать нормальный календарь
        [sg.Text("Комментарий", font=font_button), sg.Input()],
        [sg.Button("Сохранить", font=font_button, button_color='green')],
        [sg.Button("Назад", font=font_button)]
    ]

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)
    window.finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        if event == "Сохранить":
            print("Сохранение")
            window.close()
            return
        elif event == "Назад":
            window.close()
            return