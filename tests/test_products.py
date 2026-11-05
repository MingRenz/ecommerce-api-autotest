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


@pytest.mark.parametrize(
    "product_id,expect",
    [
        pytest.param(1, 200,id="normal"),
        pytest.param(999, 422,id="error"),
    ]
)
def test_get_product(product_api, product_id, expect):
    response = product_api.get_product(product_id)

    assert response.status_code == int(expect)

