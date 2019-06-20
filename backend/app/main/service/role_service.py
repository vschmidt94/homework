import datetime

from app.main import db
from app.main.model.role import Role


def save_new_role(data):
    role = Role.query.filter_by(rolename=data['rolename']).first()
    if not role:
        new_role = Role(
            rolename=data['rolename'],
            description=data['description'],
            created_on=datetime.datetime.utcnow()
        )
        save_changes(new_role)
        response_object = {
            'status': 'success',
            'message': 'Successfully created role.',
            'id': str(new_role.id)
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Role already exists. Not created.',
        }
        return response_object, 409


def get_all_roles():
    return Role.query.all()


def get_a_role(id):
    return Role.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
