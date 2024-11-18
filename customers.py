import PySimpleGUI as sg
from screeninfo import get_monitors

from customer_add import customers_add

def customers(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    mas_customers = []
    for customer in app.customers_:
        mas_customers.append(customer['organization'])

    layout = [
        [sg.Text("Клиенты", justification='center', font=font_title, size=(monitor.width, 5),
                 pad=((0, 0), (50, 0)))],
        [sg.Text("Организация / ФИО / дата начала сотрудничества", font=font_button), sg.Button("Добавить", font=font_button)],
        [sg.Listbox(mas_customers, size=(monitor.width, 10), font=font_button, key='-LIST-')],
        [sg.Button("Назад", font=font_button)]
    ]

    size_layout = (monitor.width, monitor.height - 1)
    window = sg.Window(title, layout, size=size_layout, resizable=False, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        if event == "Добавить":
            window.Hide()
            app = customers_add(app)
            new_mas_customers = []
            for customer in app.customers_:
                new_mas_customers.append(customer['organization'])
            window['-LIST-'].update(new_mas_customers)
            window.UnHide()
        elif event == "Назад":
            window.close()
            return app