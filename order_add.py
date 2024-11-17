import PySimpleGUI as sg
from screeninfo import get_monitors


def orders_add(
        order_register_date_fill,
        order_accomplishment_date_fill,
        customer_fill,
        timer_product_fill,
        product_amount_fill,
):
    monitor = get_monitors()[0]
    sg.theme("DarkGreen7")

    size_button = (25, 5)
    font_title = ('New Roman', 30)
    font_button = ('New Roman', 20)

    title = 'ЗАО "Лесозавод №10 Белка"'

    layout = [
        [sg.Text("Добавить заказ", justification='center', font=font_title, size=(monitor.width, 5),
                 pad=((0, 0), (50, 0)))],
        [sg.Text("Дата регистрации заказа:", font=font_button), sg.Input(),
         sg.Text("Дата выполнения заказа:", font=font_button), sg.Input()],
        [sg.Text("Заказчик:", font=font_button), sg.Listbox([''' список клиентов'''], font=font_button, size=(100, 2))],
        [sg.Text("Вид лесопродукции:", font=font_button), sg.Listbox([''' список лесопродукции'''], font=font_button, size=(100, 2)),
         sg.Text("Количество продукции:", font=font_button), sg.Input()],
        [sg.Text("Комментарий:", font=font_button), sg.Input()],
        [sg.Text("Статус:", font=font_button), sg.Listbox([''' список возможных статусов'''], font=font_button, size=(100, 2))],
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
            print("Сохранение")
            window.close()
            return
        elif event == "Назад":
            window.close()
            return