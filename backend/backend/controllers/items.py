from flask import Blueprint
from flask import request

from backend.db.models import Item
from backend.serializers import ItemSchema

bp = Blueprint("items", __name__, url_prefix="/items")


@bp.route("/", methods=("GET",))
def index():
    return ItemSchema().dump(Item.select().order_by(Item.name), many=True)


@bp.route("/<int:item_id>", methods=("GET",))
def get_item_by_id(item_id):
    return ItemSchema().dump(Item.get_by_id(item_id))


@bp.route("/", methods=("POST",))
def post_item():
    return [ItemSchema().load(request.get_json()).save()]


@bp.route("/<int:item_id>", methods=("POST", "PUT", "PATCH"))
def patch_item(item_id):
    requested_item = ItemSchema().load(request.get_json())
    requested_item.id = item_id
    return [requested_item.save()]


@bp.route("/<int:item_id>", methods=("DELETE",))
def delete_item(item_id):
    return [Item.get_by_id(item_id).delete_instance()]
