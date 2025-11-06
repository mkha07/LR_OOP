import datetime
from typing import List, Dict
from order import Order
from store import Store
from furniture import Furniture
from client import Client
from office_admin import OfficeAdministrator
from report import write_overdue_report


class FurnitureDeliverySystem:
    def __init__(self, system_id: int, office_name: str, admin: OfficeAdministrator):
        self.system_id = system_id
        self.office_name = office_name
        self.admin = admin
        self.orders: List[Order] = []
        self.stores: List[Store] = []
        self.furniture_types: List[Furniture] = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def add_store(self, store: Store):
        self.stores.append(store)

    def add_furniture(self, furniture: Furniture):
        self.furniture_types.append(furniture)

    def read_stores(self, stores_fname):
        with open(stores_fname, "r", encoding="utf-8") as stores_f:
            for line in stores_f:
                line = line.strip()
                if line:
                    store_id, city, address, director = line.split(";")
                    store_id = int(store_id)
                    store = Store(store_id, city, address, director)
                    self.stores.append(store)

    def read_furniture(self, furniture_fname):
        with open(furniture_fname, "r", encoding="utf-8") as furniture_f:
            for line in furniture_f:
                line = line.strip()
                if line:
                    furniture_id, weight, furniture_type, price, quantity = line.split(";")
                    furniture_id = int(furniture_id)
                    weight = float(weight)
                    price = float(price)
                    furniture = Furniture(furniture_id, weight, furniture_type, price, quantity)
                    self.furniture_types.append(furniture)

    def read_orders(self, orders_fname):
        with open(orders_fname, "r", encoding="utf-8") as orders_f:
            for line in orders_f:
                line = line.strip()
                if not line:
                    continue
                order_id_s, client_name, client_phone, planned_date_s, status, items_s = line.split(";")
                order_id = int(order_id_s)
                planned_date = datetime.datetime.strptime(planned_date_s, "%Y-%m-%d")
                client = Client(order_id, client_name, client_phone)
                items: List[Furniture] = []
                if items_s:
                    parts = items_s.split(",")
                    furniture_by_id: Dict[int, Furniture] = {f.furniture_id: f for f in self.furniture_types}
                    for p in parts:
                        fid_s, qty_s = p.split(":")
                        fid = int(fid_s)
                        qty = int(qty_s)
                        if fid in furniture_by_id:
                            base = furniture_by_id[fid]
                            items.append(
                                Furniture(base.furniture_id, base.weight, base.furniture_type, base.price, qty))
                order = Order(order_id, client, items, datetime.datetime.now(), planned_date)
                order.status = status
                self.orders.append(order)

    def is_overdue(self, order: Order, today: datetime.datetime | None = None) -> bool:
        if today is None:
            today = datetime.datetime.now()
        if order.actual_delivery_date is not None:
            return False
        return order.planned_delivery_date < today

    def aggregate_overdue_by_furniture_type(self) -> Dict[str, int]:
        result: Dict[str, int] = {}
        for order in self.orders:
            if self.is_overdue(order):
                for item in order.items:
                    result[item.furniture_type] = result.get(item.furniture_type, 0) + int(item.quantity)
        return result


if __name__ == "__main__":
    admin = OfficeAdministrator(1, "Центральный офис")
    system = FurnitureDeliverySystem(1, "Центральный офис", admin)
    system.read_furniture("furniture.txt")
    system.read_stores("store.txt")
    system.read_orders("order.txt")

    aggregated = system.aggregate_overdue_by_furniture_type()
    output = write_overdue_report(aggregated, "overdue_report.xlsx")
