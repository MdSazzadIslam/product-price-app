import pytest
from fastapi import HTTPException
from typing import List
from unittest.mock import patch, MagicMock
from app import get_prices
from app import external_api, price_trends, schemas


def test_get_products(api_client):
    response = api_client.get("/products")
    assert response.status_code == 200
    assert response.json() == []


@pytest.fixture
def mock_fetch_price_data():
    # Mock fetch_price_data function to return sample data
    mock_data = [
        {
            "product_id": 1,
            "product_name": "Product A",
            "price": 10.0,
            "updated_at": "2024-07-03T10:00:00Z",
        },
        {
            "product_id": 2,
            "product_name": "Product B",
            "price": 15.0,
            "updated_at": "2024-07-03T11:00:00Z",
        },
    ]
    return MagicMock(return_value=mock_data)


@pytest.fixture
def mock_calculate_price_trends():
    # Mock calculate_price_trends function to return sample trends
    mock_trends = [
        schemas.PriceResponse(
            product="Product A", price=10.0, currency="EUR", daily_change="FLAT"
        ),
        schemas.PriceResponse(
            product="Product B", price=15.0, currency="EUR", daily_change="UP"
        ),
    ]
    return MagicMock(return_value=mock_trends)


@patch("app.external_api.fetch_price_data", mock_fetch_price_data)
@patch("app.price_trends.calculate_price_trends", mock_calculate_price_trends)
def test_get_prices_successful(mock_fetch_price_data, mock_calculate_price_trends):
    # Test successful retrieval of prices and trends
    response = get_prices()
    assert len(response) == 2
    assert response[0].product == "Product A"
    assert response[1].product == "Product B"
    assert response[0].price == 10.0
    assert response[1].price == 15.0


@patch("app.external_api.fetch_price_data", side_effect=Exception("Mocked error"))
def test_get_prices_exception(mock_fetch_price_data):
    # Test exception handling when fetching price data
    with pytest.raises(HTTPException) as exc_info:
        get_prices()

    assert exc_info.value.status_code == 502
    assert "Error fetching data from external API" in exc_info.value.detail
