from pydantic import BaseModel


class ItemModel(BaseModel):
    id: int
    name: str
    price: float
    weight: float
    quantity_in_stock: int


class ItemCreateModel(BaseModel):
    name: str
    price: float
    weight: float
    quantity_in_stock: int


class ItemUpdateModel(BaseModel):
    name: str
    price: float
    quantity_in_stock: int
