from marshmallow import fields
from .base import BaseSchema


class ItemSchema(BaseSchema):
    equip_slot = fields.Str()
    name = fields.Str()
    supported_modifiers = fields.Integer()
