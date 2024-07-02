import pydantic
from typing import Optional


class ProductRead(pydantic.BaseModel):
    key: str
    name: str
    active: bool


class ProductCreate(pydantic.BaseModel):
    name: str
    active: bool = True


class ProductUpdate(ProductRead):
    pass


class PriceEntry(pydantic.BaseModel):
    product_id: int
    product_name: str
    price: float
    updated_at: str


class PriceResponse(pydantic.BaseModel):
    product: str
    price: float
    currency: str = "EUR"
    daily_change: Optional[str]
