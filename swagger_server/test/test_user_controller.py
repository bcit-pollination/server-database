# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.voting_token import VotingToken  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_app_create_user(self):
        """Test case for app_create_user

        Create user
        """
        body = None
        response = self.client.open(
            '/api/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Get user info
        """
        response = self.client.open(
            '/api/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_voting_token(self):
        """Test case for get_voting_token

        Get token used to vote
        """
        response = self.client.open(
            '/api/user/voting_token',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_user(self):
        """Test case for remove_user

        Remove user from service. Only a user can remove himself, hence the user is infered from the JWT
        """
        response = self.client.open(
            '/api/user',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Update user info
        """
        body = User()
        response = self.client.open(
            '/api/user',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
