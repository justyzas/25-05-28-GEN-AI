from pydantic import BaseModel, Field


class ItemModel(BaseModel):
    name: str
    code: str
    quantity: float
    measurement_unit: str  = Field(description="measurement unit if provided. If not provided use \"pcs\"")
    discount: float
    price: float
    vat: float

class InvoiceModel(BaseModel):
    is_invoice: bool 
    invoice_number: str  = Field(description="Invoice number. If not present in invoice, use \"\"")
    invoice_date: str  = Field(description="Invoice date in format yyyy-MM-dd")
    payment_due_date: str  = Field(description="Payment due date in format yyyy-MM-dd")
    vendor_name: str
    customer_name: str
    currency_code: str
    items: list[ItemModel]
    subtotal: float
    sales_tax: float
    total: float
