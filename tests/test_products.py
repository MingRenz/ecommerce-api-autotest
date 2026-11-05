import pytest


@pytest.mark.smoke
def test_get_products(product_api):
    response = product_api.get_products()

    assert response.status_code == 200

    products = response.json()

    assert isinstance(products, list)
    assert len(products) > 0

    for product in products:
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "stock" in product