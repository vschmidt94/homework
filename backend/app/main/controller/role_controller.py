from flask import request
from flask_restplus import Resource

from ..util.dtos import RoleDto
from ..service.role_service import save_new_role, get_all_roles, get_a_role

api = RoleDto.api
_role = RoleDto.role


@api.route('/')
class RoleList(Resource):
    @api.doc('list_of_registered_roles')
    @api.marshal_list_with(_role, envelope='data')
    def get(self):
        """List all roles"""
        return get_all_roles()

    @api.response(201, 'Role successfully created.')
    @api.doc('create a new role')
    @api.expect(_role, validate=True)
    def post(self):
        """Creates a new Role """
        data = request.json
        return save_new_role(data=data)


@api.route('/<id>')
@api.param('id', 'The Role identifier')
@api.response(404, 'Role not found.')
class Role(Resource):
    @api.doc('get a role')
    @api.marshal_with(_role)
    def get(self, id):
        """get a role given its identifier"""
        role = get_a_role(id)
        if not role:
            api.abort(404)
        else:
            return role
