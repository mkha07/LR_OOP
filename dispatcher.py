import datetime
from typing import List
from order import Order


class Dispatcher:
    """

    """

    def __init__(self, dispatcher_id: int, name: str, phone: str):
        self.dispatcher_id = dispatcher_id
        self.name = name
        self.phone = phone
        self.orders: List[Order] = []

    def deliver_order(self, order: Order):
        order.status = "Доставлен"
        order.actual_delivery_date = datetime.datetime.now()
        return order

    def cancel_order(self, order: Order, reason: str):
        order.status = "Отменен"
        order.cancellation_reason = reason
        return order
