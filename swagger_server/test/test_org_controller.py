# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.org import Org  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgController(BaseTestCase):
    """OrgController integration test stubs"""

    def test_create_org(self):
        """Test case for create_org

        Create org
        """
        body = Body()
        response = self.client.open(
            '/api/org',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disband_org(self):
        """Test case for disband_org

        Disband org
        """
        response = self.client.open(
            '/api/org',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org(self):
        """Test case for get_org

        Get org info
        """
        body = None
        response = self.client.open(
            '/api/org/get',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org_list(self):
        """Test case for get_org_list

        Get org info
        """
        response = self.client.open(
            '/api/org/get/list',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_org(self):
        """Test case for update_org

        Update org info
        """
        body = Org()
        response = self.client.open(
            '/api/org',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
