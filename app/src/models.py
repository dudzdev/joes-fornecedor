from decimal import Decimal

from pydantic import BaseModel


class Product(BaseModel):
    cod: int
    name: str
    unit: str
    price: Decimal

    def get_name(self):
        return self.name

    def get_cod(self):
        return self.cod

    def get_unit(self):
        return self.unit

    def get_price(self):
        return self.price
