import PySimpleGUI as sg
from screeninfo import get_monitors

from order_add import orders_add

def orders(app):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    font_title = ('New Roman', 30)
    font_button = ('New Roman', 15)

    title = 'ЗАО "Лесозавод №10 Белка"'

    def get_color_by_status(status):
        if status == "Черновик":
            return "white"
        elif status == "Согласован с клиентом":
            return "orange"
        elif status == "Принят в производство":
            return "yellow"
        elif status == "Выполнен":
            return "green"
        else:
            return "white"

    def get_orders_data():
        # Например, заказы
        orders_data = []
        for order in app.orders_:
            orders_data.append(
                {
                    "uid": order['uid'],
                    "registration_date": order['data_registration'],
                    "completion_date": order['data_completion'],
                    "customer": order['customer'],
                    "product": order['timber_product'],
                    "quantity": order['cnt_timber_product'],
                    "status": order['status'],
                    "comment": order['comment']
                }
            )
        return orders_data


    def generate_listbox_elements(orders_data):
        listbox_elements = []
        for i, order in enumerate(orders_data):
            button_text = (
                f"{order['registration_date']} / {order['completion_date']} / {order['customer']} / "
                f"{order['product']} / {order['quantity']} / {order['status']}\n"
                f"{order['comment']}"
            )
            color = get_color_by_status(order["status"])
            listbox_elements.append(
                [sg.Button(button_text, button_color=("black", color), font=font_button, size=(int(monitor.width / 16), 3),
                           key=f"-ORDER-{i}-", pad=(0, 5), border_width=5)]
            )
        return listbox_elements

    # Инициализация первого лейаута
    orders_data = get_orders_data()
    listbox_elements = generate_listbox_elements(orders_data)

    layout = [
        [sg.Text("Заказы", justification='center', font=font_title, pad=((0, 0), (20, 10)), size=(monitor.width, 2))],
        [sg.Text("Дата регистрации / Дата выполнения / Заказчик / Продукция / Кол-во / Статус", font=font_button)],
        [sg.Column(listbox_elements, scrollable=True, size=(monitor.width, 500), vertical_scroll_only=True, key='-LIST-')],
        [sg.Button("Добавить", font=font_button, size=(15, 1)), sg.Button("Назад", font=font_button, size=(15, 1))]
    ]

    size_layout = (monitor.width, monitor.height - 1)
    window = sg.Window(title, layout, size=size_layout, resizable=False, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit(1)

        if event == "Добавить":
            window.Hide()
            app = orders_add(app, "", "", "", "", "", "", "", "")
            window.close()
            orders_data = get_orders_data()
            listbox_elements = generate_listbox_elements(orders_data)
            layout = [
                [sg.Text("Заказы", justification='center', font=font_title, pad=((0, 0), (20, 10)), size=(monitor.width, 2))],
                [sg.Text("Дата регистрации / Дата выполнения / Заказчик / Продукция / Кол-во / Статус",
                         font=font_button)],
                [sg.Column(listbox_elements, scrollable=True, size=(monitor.width - 50, 500), vertical_scroll_only=True,
                           key='-LIST-')],
                [sg.Button("Добавить", font=font_button, size=(15, 1)),
                 sg.Button("Назад", font=font_button, size=(15, 1))]
            ]
            window = sg.Window(title, layout, size=size_layout, resizable=False, finalize=True)
        elif event == "Назад":
            return app

        elif event.startswith('-ORDER-'):
            order_index = int(event.split("-")[-2])
            selected_order = orders_data[order_index]
            uid = selected_order['uid']
            order_register_date = selected_order['registration_date']
            order_accomplishment_date = selected_order['completion_date']
            customer_name = selected_order['customer']
            timer_product = selected_order['product']
            product_amount = selected_order['quantity']
            status = selected_order['status']
            comment = selected_order['comment']
            window.Hide()
            app = orders_add(app, uid, order_register_date, order_accomplishment_date, customer_name, timer_product, product_amount, comment, status)
            window.close()
            orders_data = get_orders_data()
            listbox_elements = generate_listbox_elements(orders_data)
            layout = [
                [sg.Text("Заказы", justification='center', font=font_title, pad=((0, 0), (20, 10)), size=(monitor.width, 2))],
                [sg.Text("Дата регистрации / Дата выполнения / Заказчик / Продукция / Кол-во / Статус",
                         font=font_button)],
                [sg.Column(listbox_elements, scrollable=True, size=(monitor.width - 50, 500), vertical_scroll_only=True,
                           key='-LIST-')],
                [sg.Button("Добавить", font=font_button, size=(15, 1)),
                 sg.Button("Назад", font=font_button, size=(15, 1))]
            ]
            window = sg.Window(title, layout, size=size_layout, resizable=False, finalize=True)