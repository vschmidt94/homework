from flask_restplus import Namespace, fields


class UserDto:
    """
    User Data Transfer Object

    Responsible for transfering user data between objects.
    """
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })