"""Class should be opened for extension and closed for mutations

Example: Calculate price with discounts
"""


from abc import ABC, abstractmethod

class GoodDiscountCounter(ABC):
    @abstractmethod
    def apply_discount(self, price: int) -> float | int:
        pass

class PercentageDiscount(GoodDiscountCounter):
    def apply_discount(self, price: int) -> float | int:
        return price * 0.9

class FixedDiscount(GoodDiscountCounter):
    def apply_discount(self, price: int) -> float | int:
        return price - 10

def calculate_price(price: int, discount: type(GoodDiscountCounter)):
    return discount().apply_discount(price)


if __name__ == "__main__":
    price = 22
    calculate_price(price=price, discount=PercentageDiscount)
    percentage = calculate_price(price=price, discount=PercentageDiscount)
    print(percentage)

    fixed = calculate_price(price=price, discount=FixedDiscount)
    print(price)
