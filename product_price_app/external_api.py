import requests
from fastapi import HTTPException
from typing import List
from . import schemas
import logging

logger = logging.getLogger(__name__)

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
            except ValueError as ve:
                logger.warning("Skipping invalid entry: %s. Reason: %s", entry, ve)

        return valid_entries

    except requests.exceptions.RequestException as req_ex:
        error_message = f"Error fetching data from external API: {req_ex}"
        logger.error(error_message)
        raise HTTPException(
            status_code=502, detail="Error fetching data from external API"
        ) from req_ex

    except ValueError as val_err:
        error_message = f"Invalid data received from external API: {val_err}"
        logger.error(error_message)
        raise HTTPException(
            status_code=502, detail="Invalid data received from external API"
        ) from val_err

    except Exception as ex:
        error_message = f"Unexpected error during data fetch: {ex}"
        logger.error(error_message)
        raise HTTPException(
            status_code=500, detail="Unexpected error during data fetch"
        ) from ex
