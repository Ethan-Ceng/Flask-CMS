from flask import Blueprint
from app.api.v1 import user, book, client, token


def create_blueprint():
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1, url_prefix='/client')
    user.api.register(bp_v1, url_prefix='/user')
    book.api.register(bp_v1, url_prefix='/book')
    book.api.register(bp_v1, url_prefix='/token')

    return bp_v1
