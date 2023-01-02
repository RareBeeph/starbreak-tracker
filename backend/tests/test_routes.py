def test_root(test_client) -> None:
    response = test_client.get("/")

    assert response.status_code == 200
    assert b"Hello, world" in response.data
