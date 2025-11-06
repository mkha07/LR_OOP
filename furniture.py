class Furniture:
    """

    """
    def __init__(self, furniture_id: int, weight: float, furniture_type: str, price: float, quantity: int = 1):
        self.furniture_id = furniture_id
        self.weight = weight
        self.furniture_type = furniture_type
        self.price = price
        self.quantity = quantity
