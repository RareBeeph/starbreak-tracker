from backend.app import app
import pytest


@pytest.fixture(scope="module")
def test_client() -> None:
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
