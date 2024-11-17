import PySimpleGUI as sg
from screeninfo import get_monitors

from section_commerce import section_commerce
from section_production import section_production
from timber_products import timber_products

def service(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Выберите службу", justification='center', font=font_title, size=(monitor.width, 5), pad=((0, 0), (50, 0)))],
        [sg.Push(), sg.Button("Коммерция", size=size_button, font=font_button, border_width=5),
         sg.Button("Производство", size=size_button, font=font_button, border_width=5),
         sg.Button("Технолог", size=size_button, font=font_button, border_width=5), sg.Push()]
    ]

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=True, finalize=True)
    window.finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Коммерция":
            window.Hide()
            section_commerce(app)
            window.UnHide()
        elif event == "Производство":
            window.Hide()
            section_production(app)
            window.UnHide()
        elif event == "Технолог":
            window.Hide()
            timber_products(app)
            window.UnHide()

    window.close()