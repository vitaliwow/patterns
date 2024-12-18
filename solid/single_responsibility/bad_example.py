"""Class should be responsible for a particular task

Example: You are creating an order service.
"""

class OrderExample:
    """Good example of realization

    The Order class only calculates items
    Other classes use order instances to process that one in any cases
    """

class Order:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def calculate_total(self) -> int:
        # Calculates Order
        return self.x + self.y

class OrderRepository:
    def save_to_database(self, order: Order):
        # changing logics do not require changes in saving
        print(f"{id(order)} saved!")

class OrderPrinter:
    def print_order(self, order: Order):
        # changing logics do not require changes in printing
        print(f"{id(order)} is printed")


if __name__ == "__main__":
    order = Order(2, 3)
    print("Calculated order total is", order.calculate_total())

    OrderRepository().save_to_database(order)
    OrderPrinter().print_order(order)
