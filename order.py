from datetime import datetime
from typing import List, Optional
from client import Client
from furniture import Furniture


class Order:
    """

    """
    def __init__(self, order_id: int, client: Client, items: List[Furniture],
                 order_date: datetime, planned_delivery_date: datetime):
        self.order_id = order_id
        self.client = client
        self.items = items
        self.order_date = order_date
        self.planned_delivery_date = planned_delivery_date
        self.actual_delivery_date: Optional[datetime] = None
        self.status = "Обрабатывается"
        self.cancellation_reason: Optional[str] = None
