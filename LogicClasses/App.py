from dataclasses import dataclass

from LogicClasses.Customer import Customer
from LogicClasses.Order import Order
from LogicClasses.TimberProducts import TimberProducts

@dataclass
class App:
    customers_: Customer
    orders_: Order
    timber_products_: TimberProducts