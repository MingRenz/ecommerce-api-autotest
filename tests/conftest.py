import os

import pytest

from client.http_client import HttpClient
from api.product_api import ProductApi


@pytest.fixture
def http_client():
    base_url = os.getenv(
        "BASE_URL",
        "http://127.0.0.1:8000"
    )

    client = HttpClient(base_url)

    yield client

    client.close()


@pytest.fixture
def product_api(http_client):
    return ProductApi(http_client)