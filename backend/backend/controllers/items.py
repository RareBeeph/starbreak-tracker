from flask import Blueprint

from backend.db.models import Item
from backend.serializers import ItemSchema

bp = Blueprint("items", __name__, url_prefix="/items")


@bp.route("/", methods=("GET",))
def index():
    return ItemSchema().dump(Item.select().order_by(Item.name), many=True)
