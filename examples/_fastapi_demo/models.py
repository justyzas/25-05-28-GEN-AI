from pydantic import BaseModel


class ItemModel(BaseModel):
    name: str
    price: float
    weight: float
    quantity_in_stock: int
