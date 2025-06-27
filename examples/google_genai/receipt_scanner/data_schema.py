from pydantic import BaseModel, Field
from typing import Literal

class ProductInformation(BaseModel):
    name: str | None = Field(description="Product name if there is one")
    quantity: float | None
    price: float | None
    # total: float | None # Optional (you can compute it later)

class ReceiptInformation(BaseModel):
    seller_name: str|None
    total_discount: float
    price_without_vat: float
    total: float
    date: str
    payment_method: Literal["CASH", "CREDIT", "BITCOIN", "UNKNOWN"] = Field(description="Payment method. If word like \"Grynieji\" is found, assume it's cash. If there is no payment method found, please give me unknown")
    products: list[ProductInformation]
