import mallard
import time
from typing import List
from mallard.order import Order


class Customer:
    def __init__(
        self,
        name: str,
        id: int,
        orders: List[Order],
    ):
        self.name = name
        self.id = id
        self.orders = orders

    # We can write two __init__ constructor methods with different parameters
    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
    ):
        self.name = name
        self.phone = phone
        self.email = email
        self.orders = []
        # TODO: A better ID system - For now, I'm just using the system time, up to 100'th of a second (just the last 6 digits)
        self.id = int(time.time() * 100) % 1000000
