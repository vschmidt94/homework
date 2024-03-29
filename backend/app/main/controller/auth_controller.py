from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dtos import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

# RVW: Mentioned elsewhere, hook up a PEP8 formatter and linter.

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """

    @api.doc('user login')
    #RVW: Realized I should be expecting a model. The DTO model may not be
    #     the right one, don't know why I commented this one out.
    #@api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """

    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
