from datetime import datetime
from typing import List
from order import Order


class OfficeAdministrator:
    """

    """

    def __init__(self, admin_id: int, name: str):
        self.admin_id = admin_id
        self.name = name
        self.received_orders: List[Order] = []

    def accept_order(self, order: Order, planned_delivery_date: datetime):
        self.received_orders.append(order)
        order.status = "В доставке"
        order.planned_delivery_date = planned_delivery_date
        return order
