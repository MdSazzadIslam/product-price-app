"""Database models (not really)."""

import dataclasses


@dataclasses.dataclass
class Product:
    id: int
    key: str
    name: str
    active: bool = True
