"""Class should be opened for extension and closed for mutations

Example: Calculate price with discounts
"""


class BadDiscountCounter:
    """The class depends on the type of discount"""

    def apply_discount(self, price: int, discount_type: str) -> int | float:
        if discount_type == 'percentage':
            return price * 0.9
        elif discount_type == 'fixed':
            return price - 10
