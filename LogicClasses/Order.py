from dataclasses import dataclass


@dataclass
class Order:
    uid: str
    data_registration: str
    data_completion: str
    customer: str
    timber_product: str
    cnt_timber_product: int
    comment: str
    status: str