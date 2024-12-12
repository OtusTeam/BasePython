class Product(BaseModel):
    name: str
    price: float
    description: str | None = None
    image_url: str

    @validator('price')
    def check_quantity(cls, value):
        if value < 10:
            raise ValueError("Quantity must be greater than 0")
        return value
