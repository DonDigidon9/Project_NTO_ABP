from dataclasses import dataclass


@dataclass
class Customer:
    organization: str
    fio: str
    add_data: str
    comment: str