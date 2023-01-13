from marshmallow import fields
from marshmallow import post_load

from backend.db.models.item import Item
from .base import BaseSchema


class ItemSchema(BaseSchema):
    equip_slot = fields.Str()
    name = fields.Str()
    supported_modifiers = fields.Integer()

    @post_load
    def make_item(self, data, **kwargs):
        return Item(**data)
