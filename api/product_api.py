class ProductApi:

    def __init__(self, client):
        self.client = client

    def get_products(self):
        return self.client.request("GET", "/products")

    def get_product(self, product_id):
        return self.client.request(
            "GET",
            f"/products/{product_id}"
        )