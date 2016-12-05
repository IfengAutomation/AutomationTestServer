from flask import Blueprint

cases = Blueprint('cases', __name__, url_prefix='/cases')


@cases.route('/')
def root():
    return 'CASES ROOT'
