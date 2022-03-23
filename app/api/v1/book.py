from app.utils.redprint import Redprint

api = Redprint('book')


@api.route('/search')
def get_book():
    return 'get book'
