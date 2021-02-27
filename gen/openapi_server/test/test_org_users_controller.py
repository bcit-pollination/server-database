# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from openapi_server.models.inline_response404 import InlineResponse404  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrgUsersController(BaseTestCase):
    """OrgUsersController integration test stubs"""

    def test_accept_org_invite(self):
        """Test case for accept_org_invite

        Accept invitation user to org
        """
        query_string = [('encrypted_data', 56)]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/users/invite/accept',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_change_user_privilege(self):
        """Test case for change_user_privilege

        Change user privileges
        """
        unknown_base_type = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/users/privileges',
            method='PUT',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org_users(self):
        """Test case for get_org_users

        Fetch org users
        """
        query_string = [('org_id', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/users',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_kick_org_user(self):
        """Test case for kick_org_user

        Kick user from org
        """
        unknown_base_type = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/users/delete',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_org_invite_user(self):
        """Test case for org_invite_user

        Add user to org
        """
        unknown_base_type = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/users/invite',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
