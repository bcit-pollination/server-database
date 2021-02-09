# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.verifier_password import VerifierPassword  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgController(BaseTestCase):
    """OrgController integration test stubs"""

    def test_create_org(self):
        """Test case for create_org

        Create org
        """
        body = None
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
        query_string = [('org_id', 56)]
        response = self.client.open(
            '/api/org',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org_list(self):
        """Test case for get_org_list

        Get org info
        """
        response = self.client.open(
            '/api/org/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_verifier_password(self):
        """Test case for get_verifier_password

        Get password used by ID verifiers to login into voting machine
        """
        body = None
        response = self.client.open(
            '/api/org/verifier_password',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_org(self):
        """Test case for update_org

        Update org info
        """
        body = None
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
