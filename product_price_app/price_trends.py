from typing import List
from enum import Enum
from . import schemas


class PriceChange(str, Enum):
    SLIGHTLY_UP = "SLIGHTLY UP"
    UP = "UP"
    SHARPLY_UP = "SHARPLY UP"
    SLIGHTLY_DOWN = "SLIGHTLY DOWN"
    DOWN = "DOWN"
    SHARPLY_DOWN = "SHARPLY DOWN"


def calculate_percentage_change(opening_price: float, final_price: float) -> float:
    if opening_price == 0:
        return 0.0
    return ((final_price - opening_price) / opening_price) * 100


def calculate_price_trends(
    price_data: List[schemas.PriceEntry],
) -> List[schemas.PriceResponse]:
    prices_map = {}

    # Process price data to determine opening and final prices
    for price_entry in price_data:
        product_id = price_entry.product_id
        product_name = price_entry.product_name
        price = price_entry.price
        updated_at = price_entry.updated_at

        if product_id not in prices_map:
            # First occurrence of the product, consider it as opening price
            prices_map[product_id] = {
                "product_name": product_name,
                "opening_price": price,
                "final_price": price,
                "updated_at": updated_at,
            }
        else:
            # Update final price if there's a subsequent entry
            prices_map[product_id]["final_price"] = price
            prices_map[product_id]["updated_at"] = updated_at

    # Prepare response based on opening and final prices
    response_data = []
    for product_id, data in prices_map.items():
        opening_price = data["opening_price"]
        final_price = data["final_price"]

        # Calculate percentage change
        percentage_change = calculate_percentage_change(opening_price, final_price)

        # Determine trend category
        if percentage_change > 15:
            trend = PriceChange.SHARPLY_UP
        elif percentage_change > 5:
            trend = PriceChange.UP
        elif percentage_change < -15:
            trend = PriceChange.SHARPLY_DOWN
        elif percentage_change < -5:
            trend = PriceChange.DOWN
        elif percentage_change == 0:
            trend = None  # No change
        elif percentage_change < 0:
            trend = PriceChange.SLIGHTLY_DOWN
        else:
            trend = PriceChange.SLIGHTLY_UP

        # Prepare response format
        response_entry = schemas.PriceResponse(
            product=data["product_name"],
            price=final_price,
            currency="EUR",
            daily_change=trend.value if trend else None,
        )
        response_data.append(response_entry)

    return response_data
