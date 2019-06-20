# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.role_controller import api as role_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTful API for Users and Roles',
          version='1.0',
          description='Homework Project'
          )

api.add_namespace(user_ns, path='api/user')
api.add_namespace(role_ns, path='api/role')
api.add_namespace(auth_ns)

from .main.views import views
