import json
from dataclasses import asdict

import PySimpleGUI as sg
from screeninfo import get_monitors

from LogicClasses.App import App
from LogicClasses.Order import Order

def open_window_fail():
    layout_fail = [[sg.Text("Проверьте правильность введенных данных", font=('New Roman', 20))], [sg.OK(key='-OK-')]]
    window_fail = sg.Window("", layout_fail)

    while True:
        event_fail, values_fail = window_fail.read()
        if event_fail in (sg.WIN_CLOSED, '-OK-'):
            break
    window_fail.close()

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

    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    mas_customer = []
    for customer in app.customers_:
        mas_customer.append(customer['organization'])
    mas_timber_product = []
    for timber_product in app.timber_products_:
        mas_timber_product.append(timber_product['name'])
    mas_status = ['Черновик', 'Согласован с клиентом', 'Принят в производство', 'Выполнен']
    title_window = "Добавить заказ"
    if order_register_date_fill != "":
        title_window = "Изменить заказ"

    customer_listbox_visible = False
    timber_listbox_visible = False
    status_listbox_visible = False

    layout = [
        [sg.Text(title_window, justification='center', font=font_title, size=(monitor.width, 2),
                 pad=((0, 0), (10, 0)))],
        [sg.Text("Дата регистрации заказа:", font=font_button, size=(25, 1)),
         sg.InputText(default_text=order_register_date_fill, size=(15, 1), font=font_button, key='-DATA_REGISTRATION-', disabled_readonly_background_color='green', disabled=True),
         sg.Button("Дата", font=font_button, key='-DATA_REG-'),
         sg.Push(),
         sg.Text("Дата выполнения заказа:", font=font_button, size=(25, 1)),
         sg.InputText(default_text=order_accomplishment_date_fill, size=(15, 1), font=font_button, key='-DATA_COMPLETION-', disabled_readonly_background_color='green', disabled=True),
         sg.Button("Дата", font=font_button, key='-DATA_COM-')],
        [sg.Push()],
        [sg.Text("Заказчик:", font=font_button, size=(25, 2)), sg.Listbox(mas_customer, visible=False, font=font_button, size=(100, 4), key='-CUSTOMER_LISTBOX-'),
         sg.Button("Показать варианты", key="-TOGGLE_CUSTOMER-", font=font_button)],
        [sg.Text("Вид лесопродукции:", font=font_button, size=(25, 2)), sg.Listbox(mas_timber_product, visible=False, font=font_button, size=(100, 4), key='-TIMBER_LISTBOX-'),
         sg.Button("Показать варианты", key="-TOGGLE_TIMBER-", font=font_button)],
        [sg.Text("Количество лесопродукции:", font=font_button, size=(25, 2)), sg.InputText(product_amount_fill, size=(15, 1), font=font_button, key="-INPUT-")],
        [sg.Text("Статус:", font=font_button, size=(25, 2)), sg.Listbox(mas_status, visible=False, font=font_button, size=(100, 4), key='-STATUS_LISTBOX-'),
         sg.Button("Показать варианты", key="-TOGGLE_STATUS-", font=font_button)],
        [sg.Text("Комментарий:", font=font_button, size=(25, 2)), sg.Multiline(default_text=comment_fill, font=font_button, size=(100, 4), key='-COMMENT-')],
        [sg.Push()],
        [sg.Button("Сохранить", font=font_button)],
        [sg.Button("Назад", font=font_button)]
    ]

    size_layout = (monitor.width, monitor.height)
    window = sg.Window(title, layout, size=size_layout, resizable=False, finalize=True)

    selected_data_reg = None
    selected_data_com = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        if event == "Сохранить":
            if ((selected_data_reg is None) or (selected_data_com is None) or
                    (selected_data_reg[2] > selected_data_com[2]) or
                    (selected_data_reg[2] == selected_data_com[2] and selected_data_reg[0] > selected_data_com[0]) or
                    (selected_data_reg[2] == selected_data_com[2] and selected_data_reg[0] == selected_data_com[0] and selected_data_reg[1] >= selected_data_com[1])):
                open_window_fail()
                continue
            try:
                cnt = int(values['-INPUT-'])
            except ValueError:
                open_window_fail()
                continue
            new_order = Order(
                data_registration=values['-DATA_REGISTRATION-'],
                data_completion=values['-DATA_COMPLETION-'],
                customer="test",
                timber_product="111",
                cnt_timber_product=cnt,
                comment=values['-COMMENT-'],
                status="Черновик"
            )
            app.orders_.append(new_order)
            json_data = json.dumps(asdict(app), indent=4)
            with open(".venv/file.json", "w") as file:
                file.write(json_data)
            window.close()
            return App(**json.loads(json_data))
        elif event == '-TOGGLE_CUSTOMER-':
            customer_listbox_visible = not customer_listbox_visible
            window["-CUSTOMER_LISTBOX-"].update(visible=customer_listbox_visible)
            window["-TOGGLE_CUSTOMER-"].update("Скрыть варианты" if customer_listbox_visible else "Показать варианты")
        elif event == '-TOGGLE_TIMBER-':
            timber_listbox_visible = not timber_listbox_visible
            window["-TIMBER_LISTBOX-"].update(visible=timber_listbox_visible)
            window["-TOGGLE_TIMBER-"].update("Скрыть варианты" if timber_listbox_visible else "Показать варианты")
        elif event == '-TOGGLE_STATUS-':
            status_listbox_visible = not status_listbox_visible
            window["-STATUS_LISTBOX-"].update(visible=status_listbox_visible)
            window["-TOGGLE_STATUS-"].update("Скрыть варианты" if status_listbox_visible else "Показать варианты")
        elif event == '-DATA_REG-':
            selected_data_reg = sg.popup_get_date()
            if selected_data_reg:
                window['-DATA_REGISTRATION-'].update(f'{selected_data_reg[1]}.{selected_data_reg[0]}.{selected_data_reg[2]}')
        elif event == '-DATA_COM-':
            selected_data_com = sg.popup_get_date()
            if selected_data_com:
                window['-DATA_COMPLETION-'].update(f'{selected_data_com[1]}.{selected_data_com[0]}.{selected_data_com[2]}')
        elif event == "Назад":
            window.close()
            return app