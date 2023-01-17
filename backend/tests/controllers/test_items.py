from backend.db.models import Item
from backend.serializers import ItemSchema
from faker import Faker


schema = ItemSchema()
resource = "/items"
fake = Faker()


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
