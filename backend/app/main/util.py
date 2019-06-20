from flask_restplus import Namespace, fields


class UserDto:
    """
    User Data Transfer Object

    Responsible for transferring user data between objects.
    """
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })


class RoleDto:
    """
    Role Data Transfer Object

    Responsible for transferring user data between objects.
    """
    api = Namespace('role', description='role related operations')
    role = api.model('role', {
        'id': fields.String(required=False, description='role id'),
        'rolename': fields.String(required=True, description='role name'),
        'description': fields.String(required=True, description='role description')
    })
