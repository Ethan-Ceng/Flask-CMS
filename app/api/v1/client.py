from flask import request, jsonify

from app.utils.error_code import ClientTypeError, Success
from app.utils.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm
from app.utils.enums import ClientTypeEnum
# from werkzeug.exceptions import HTTPException

api = Redprint('client')


@api.route('/index')
def get_book():
    return 'client index'


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
