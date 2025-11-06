from order import Order
class Director:
    """

    """

    def __init__(self, director_id: int, name: str):
        self.director_id = director_id
        self.name = name

    def process_order(self, order: Order):
        order.status = "Передан в центральный офис"
        return order
