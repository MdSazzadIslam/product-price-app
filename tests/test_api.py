def test_get_products(api_client):
    response = api_client.get("/products")
    assert response.status_code == 200
    assert response.json() == []
