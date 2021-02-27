# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserAuthController(BaseTestCase):
    """UserAuthController integration test stubs"""

    def test_login(self):
        """Test case for login

        Login user
        """
        unknown_base_type = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/user/login',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout(self):
        """Test case for logout

        Login user
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/user/logout',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
