import datetime

from app.main import db
from app.main.model.user import User
# from app.main.model.role import Role


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.user_id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        # TODO: this is hacky, figure out better approach
        if 'role_id' in data:
            roleid=data['role_id']
        else:
            roleid=None

        new_user = User(
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            username=data['username'],
            password=data['password'],
            role_id=roleid,
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(user_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()