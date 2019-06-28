from app.main.model.user import User
from ..service.blacklist_service import save_token

#RVW: ? Research - see if there's a module with all the HTTP return codes ?
#     If this were C, they would be #defines, seems odd / error prone to encode them
#     directly.
# EDIT: See Python http.HTTPStatus class - it has the codes enumerated as I am thinking
#     of and also text descriptions. Should be using that as a standardized return format,
#     (where appropriate) - plus, improves readability.

#RVW/TODO: Get more practice with JWT authorizations. Again, suspect there is existing
#     module out there that can handle most of this. Need to gain experience with other
#     implementations - this one feels very "roll your own" version of common use case.

class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.user_id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403
