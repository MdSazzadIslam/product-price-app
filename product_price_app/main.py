from typing import List
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from . import crud, exceptions, schemas, external_api, price_trends

app = FastAPI()


@app.get("/products", response_model=list[schemas.ProductRead])
def read_products():
    return crud.read_products()


@app.get(
    "/products/{product_key}",
    response_model=schemas.ProductRead,
    responses={404: {"description": "Record not found"}},
)
def read_product(product_key: str):
    return crud.read_product(product_key=product_key)


@app.post("/products", response_model=schemas.ProductRead, status_code=201)
def create_product(product: schemas.ProductCreate):
    return crud.create_product(product)


@app.put("/products/{product_key}", response_model=schemas.ProductRead)
def update_product(product_key: str, product: schemas.ProductUpdate):
    if product_key != product.key:
        raise HTTPException(status_code=400, detail="Product key cannot be changed")
    return crud.update_product(product)


@app.exception_handler(exceptions.ObjectDoesNotExist)
def object_does_not_exist_exception_handler(
    request: Request, exc: exceptions.ObjectDoesNotExist
) -> JSONResponse:
    # pylint: disable=unused-argument
    return JSONResponse(status_code=404, content={"message": str(exc)})


@app.get("/prices", response_model=List[schemas.PriceResponse], tags=["Prices"])
async def get_prices():
    """
    Retrieve current prices and their trends.

    This endpoint fetches data from an external API and calculates the price trends
    based on the fetched data. It returns a list of PriceResponse objects.

    Raises:
        HTTPException: If there is an issue fetching data or calculating trends.

    Returns:
        List[schemas.PriceResponse]: A list of PriceResponse objects representing current prices and trends.
    """
    try:
        # Fetch price data from external API
        price_data = external_api.fetch_price_data()

        # Calculate price trends
        price_trends_data = price_trends.calculate_price_trends(price_data)

        return price_trends_data

    except Exception as e:
        error_message = f"Error fetching data from external API: {str(e)}"
        raise HTTPException(status_code=502, detail=error_message) from e
