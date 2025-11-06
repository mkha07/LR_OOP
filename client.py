import datetime
from typing import List
from furniture import Furniture


class Client:
    """

    """

    def __init__(self, client_id: int, name: str, phone: str):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.current_orders: list = []

    def make_order(self, order_id: int, items: List[Furniture], delivery_date: datetime.datetime):
        order = Order(order_id, self, items, datetime.datetime.now(), delivery_date)
        self.current_orders.append(order)
        return order
