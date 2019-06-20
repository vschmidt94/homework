import unittest

from app.main import db
from app.main.model.blacklist import BlacklistToken
import json
from app.test.base import BaseTestCase

role1 = {'rolename':'Manager', 'description':'General Manager'}
role2 = {'rolename':'Employee', 'description':'Employee'}


def add_role(self, role):
    return self.client.post(
        '/role/',
        data=json.dumps(role),
        content_type='application/json'
    )


def add_roles(self, role_list):
    """ Adds a list of roles, should only be used for mass population, won't return data """
    # TODO: refactor the assertions into the add_role() case, possibly key off an expected result
    #       needs more DRYness
    for role in role_list:
        add_role(self, role)


def get_roles(self):
    return self.client.get(
        '/role/'
    )

def get_role_by_id(self, id):
    return self.client.get(
        '/role/{}'.format(id)
    )

# TODO - all test should rely on defined string messages, stop hardcoding strings inline.

class TestRoleBlueprint(BaseTestCase):

    def test_role_creation(self):
        """ Tests for role creation """
        with self.client:
            response = add_role(self, role1)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created role.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_get_roles(self):
        """ Tests for getting list of roles """
        roll_list = [role1, role2]
        with self.client:
            add_roles(self, roll_list)
            response = get_roles(self)
            data = json.loads(response.data.decode())
            self.assertEqual(len(data['data']), 2)
            # TODO: Should get more detailed here, check the returned list of roles is what was loaded.
            #       Revisit if time allows.
            self.assertTrue( data['data'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_get_role_by_id(self):
        """ Tests for getting a specific role """
        with self.client:
            response = add_role(self, role2)
            data = json.loads(response.data.decode())
            new_id = data['id']
            response = get_role_by_id(self, new_id)
            data = json.loads(response.data.decode())
            self.assertTrue(data['rolename'] == role2['rolename'])
            self.assertTrue(data['description'] == role2['description'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
