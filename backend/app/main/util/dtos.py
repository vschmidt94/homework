from flask_restplus import Namespace, fields


class UserDto:
    """
    User Data Transfer Object

    Responsible for transferring user data between objects.
    """
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'firstname': fields.String(required=True, description='user first name'),
        'lastname': fields.String(required=True, description='user last name'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'role_id': fields.String(required=False, description='role id for user'),
        'role': fields.String(required=False, description='role for user')
    })


class RoleDto:
    """
    Role Data Transfer Object

    Responsible for transferring role data between objects.
    """
    api = Namespace('role', description='role related operations')
    role = api.model('role', {
        # TODO: see if id can be removed from Swagger interface for post... need to learn that
        # RVW: id could be removed by defining a different model to use at API level.
        'id': fields.String(required=False, description='role id'),
        'rolename': fields.String(required=True, description='role name'),
        'description': fields.String(required=True, description='role description')
    })


class AuthDto:
    """
    Authentication Data Transfer Object

    Responsible for transferring auth data between objects.
    """
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
