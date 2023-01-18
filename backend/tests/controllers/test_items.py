from backend.db.models import Item
from backend.serializers import ItemSchema
from backend.db import conn
from faker import Faker
from peewee import SqliteDatabase
import pytest


schema = ItemSchema()
resource = "/items"
fake = Faker()

FILL_QUANTITY = 3


@pytest.fixture
def clean_fill_items(test_client) -> None:
    conn = SqliteDatabase("file::memory:")  # might interfere with later tests
    conn.create_tables(Item)
    for i in range(FILL_QUANTITY):  # loop runs every time the fixture is accessed
        test_client.post(
            f"{resource}/",
            json=schema.dump(
                Item(name=fake.name(), equip_slot=fake.ean(length=13)),
            ),
        )  # relies on the validity of posting via the client. avoid circular logic
    return test_client.get(f"{resource}/")  # relies on the validity of getting all rows


def test_root(test_client) -> None:
    response = test_client.get(f"{resource}/")
    assert response.status_code == 200


def test_create(test_client) -> None:
    response = test_client.post(
        f"{resource}/",
        json=schema.dump(
            Item(name=fake.name(), equip_slot=fake.ean(length=13)),
        ),
    )
    assert response.status_code == 200


def test_get_by_id(test_client, clean_fill_items) -> None:
    response = test_client.get(f"{resource}/")  # does not yet query by id
    assert response.status_code == 200
