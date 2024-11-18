import json
from dataclasses import asdict
from email.policy import default

import PySimpleGUI as sg
from screeninfo import get_monitors

from LogicClasses.Order import Order

def orders_add(app,
        order_register_date_fill,
        order_accomplishment_date_fill,
        customer_name_fill,
        timer_product_fill,
        product_amount_fill,
        comment_fill,
        status_fill
):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    headers = ["Заказчик:", "Статус:", "Вид лесопродукции:", "Количество лесопродукции:"]
    headers_column = [[sg.Text(header, font=font_button, size=(25, 2))] for header in headers]
    listbox_column = [
        [sg.Listbox([''' список заказчиков'''], font=font_button, size=(100, 2))],
        [sg.Listbox([''' список статусов'''], font=font_button, size=(100, 2))],
        [sg.Listbox([''' список лесопродукции'''], font=font_button, size=(100, 2))],
        [sg.InputText(product_amount_fill, size=(15, 1), font=font_button, key="-INPUT-")]
    ]

    layout = [
        [sg.Text("Добавить заказ", justification='center', font=font_title, size=(monitor.width, 2),
                 pad=((0, 0), (10, 0)))],
        [sg.Text("Дата регистрации заказа:", font=font_button, size=(25, 1)), sg.InputText(default_text=order_register_date_fill, size=(15, 1), font=font_button, key='-DATA_REGISTRATION-'), sg.Push(),
         sg.Text("Дата выполнения заказа:", font=font_button, size=(25, 1)), sg.InputText(default_text=order_accomplishment_date_fill, size=(15, 1), font=font_button, key='-DATA_COMPLETION-')],
        [sg.Push()],
        [sg.Text("Заказчик:", font=font_button, size=(25, 2)), sg.Listbox([''' список заказчиков'''], font=font_button, size=(100, 2))],
        [sg.Text("Вид лесопродукции:", font=font_button, size=(25, 2)), sg.Listbox([''' список лесопродукции'''], font=font_button, size=(100, 2))],
        [sg.Text("Количество лесопродукции", font=font_button, size=(25, 2)), sg.InputText(product_amount_fill, size=(15, 1), font=font_button, key="-INPUT-")],
        [sg.Text("Статус:", font=font_button, size=(25, 2)), sg.Listbox([''' список статусов'''], font=font_button, size=(100, 2))],
        [sg.Text("Комментарий:", font=font_button, size=(25, 2)), sg.Multiline(default_text=comment_fill, font=font_button, size=(100, 5), key='-COMMENT-')],
        [sg.Push()],
        [sg.Button("Сохранить", font=font_button)],
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
            new_order = Order(
                data_registration=values['-DATA_REGISTRATION-'],
                data_completion=values['-DATA_COMPLETION-'],
                customer="test",
                timber_product="111",
                cnt_timber_product=11,
                comment=values['-COMMENT-'],
                status="Черновик"
            )
            app.orders_.append(new_order)
            json_data = json.dumps(asdict(app), indent=4)
            with open("file.json", "w") as file:
                file.write(json_data)
            window.close()
            return
        elif event == "Назад":
            window.close()
            return