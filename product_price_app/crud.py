from . import database, exceptions, models, schemas


def read_products() -> list[models.Product]:
    """Read products from the database."""
    return database.products


def read_product(product_key: str) -> models.Product:
    """Read a product from the database."""
    try:
        return next(
            product
            for product in database.products
            if product.key == product_key
        )
    except StopIteration:
        # pylint: disable=raise-missing-from
        raise exceptions.ObjectDoesNotExist(
            f"Product {product_key} does not exist"
        )


def create_product(product_create: schemas.ProductCreate) -> models.Product:
    """Create a product in the database."""
    product_id = len(database.products) + 1
    product_key = (
        f"P{product_id:03d}{product_create.name.split()[0][:10].upper()}"
    )
    product = models.Product(
        id=product_id,
        key=product_key,
        name=product_create.name,
        active=product_create.active,
    )
    database.products.append(product)
    return product


def update_product(product_update: schemas.ProductUpdate) -> models.Product:
    """Update a product in the database."""
    product = read_product(product_update.key)
    product.name = product_update.name
    product.active = product_update.active
    return product
