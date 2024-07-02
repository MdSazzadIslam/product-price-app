import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from product_price_app.main import app


@pytest.fixture
def empty_database(mocker: MockerFixture) -> None:
    mocker.patch("product_price_app.database.products", new=[])


@pytest.fixture
def api_client(mocker: MockerFixture, empty_database) -> TestClient:
    return TestClient(app)
