import requests
from fastapi import HTTPException
from typing import List
from . import schemas

EXTERNAL_API_URL = "http://localhost:8081/price-feed.json"


def fetch_price_data() -> List[schemas.PriceEntry]:
    try:
        response = requests.get(EXTERNAL_API_URL)
        response.raise_for_status()
        price_data = response.json()

        # Validate and filter valid entries
        valid_entries = []
        for entry in price_data:
            try:
                price_entry = schemas.PriceEntry(**entry)
                valid_entries.append(price_entry)
            except ValueError:
                pass  # Skip invalid entries

        return valid_entries

    except Exception as e:
        error_message = f"Error fetching data from external API: {str(e)}"
        raise HTTPException(status_code=502, detail=error_message) from e
