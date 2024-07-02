"""Replacement for a database to keep things simple."""

from .models import Product

products = [
    Product(id=1, key="P001HYDRO", name="Hydro"),
    Product(id=2, key="P002SOLAR", name="Solar"),
    Product(id=3, key="P003WIND", name="Wind"),
    Product(id=4, key="P004BIOMASS", name="Biomass"),
    Product(id=5, key="P005BIOGAS", name="Biogas"),
    Product(id=6, key="P006GEOTHERMAL", name="Geothermal", active=False),
]
