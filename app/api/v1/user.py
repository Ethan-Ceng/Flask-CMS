from app.utils.redprint import Redprint
from app.utils.error_code import ClientTypeError, Success
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm
from app.utils.enums import ClientTypeEnum
# from werkzeug.exceptions import HTTPException

api = Redprint('user')


@api.route('/profile')
def get_user():
    return 'this is you profile'


@api.route('/register', methods=['POST'])
def create_client():
    print('注册请求')
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    print(form)
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
