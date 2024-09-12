from dataclasses import dataclass


@dataclass(frozen=True)
class ProductCreate:
    name: str
    price: int


@dataclass
class Product:
    id: int
    name: str
    price: int
