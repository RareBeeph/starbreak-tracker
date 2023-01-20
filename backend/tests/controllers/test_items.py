from backend.db.models import Item
from backend.serializers import ItemSchema
from faker import Faker
from peewee import SqliteDatabase
import pytest


schema = ItemSchema()
resource = "/items"
fake = Faker()

FILL_QUANTITY = 3


@pytest.fixture(autouse=True)
def clean_fill_items(test_client) -> None:
    conn = SqliteDatabase("file::memory:")
    Item._meta.database = conn
    conn.create_tables([Item])

    for i in range(FILL_QUANTITY):  # loop runs every time the fixture is accessed
        Item(name=fake.name(), equip_slot=fake.ean(length=13)).save(),
    assert Item.select().count() == FILL_QUANTITY


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


def test_get_by_id(test_client) -> None:
    i = Item.get().id
    response = test_client.get(f"{resource}/{str(i)}")
    assert response.status_code == 200


def test_patch(test_client) -> None:
    i = Item.get().id
    patch = Item(name=fake.name(), equip_slot=fake.ean(length=13))

    response = test_client.post(
        f"{resource}/{str(i)}",
        json=schema.dump(patch),
    )
    assert response.status_code == 200

    patch.id = i
    assert Item.get_by_id(i) == patch


def test_delete(test_client) -> None:
    i = Item.get().id

    response = test_client.delete(f"{resource}/{str(i)}")
    assert response.status_code == 200
    assert Item.select().where(Item.id == i).count() == 0
