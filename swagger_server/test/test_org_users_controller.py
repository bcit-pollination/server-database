# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgUsersController(BaseTestCase):
    """OrgUsersController integration test stubs"""

    def test_accept_org_invite(self):
        """Test case for accept_org_invite

        Accept invitation user to org
        """
        query_string = [('encrypted_data', 56)]
        response = self.client.open(
            '/api/org/users/invite/accept',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_change_user_privilege(self):
        """Test case for change_user_privilege

        Change user privileges
        """
        body = None
        response = self.client.open(
            '/api/org/users/privileges',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org_users(self):
        """Test case for get_org_users

        Fetch org users
        """
        body = Body1()
        response = self.client.open(
            '/api/org/users/get/list',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_kick_org_user(self):
        """Test case for kick_org_user

        Kick user from org
        """
        body = None
        response = self.client.open(
            '/api/org/users/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_org_invite_user(self):
        """Test case for org_invite_user

        Add user to org
        """
        body = None
        response = self.client.open(
            '/api/org/users/invite',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
