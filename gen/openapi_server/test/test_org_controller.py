# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from openapi_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from openapi_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.models.verifier_password import VerifierPassword  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrgController(BaseTestCase):
    """OrgController integration test stubs"""

    def test_create_org(self):
        """Test case for create_org

        Create org
        """
        unknown_base_type = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disband_org(self):
        """Test case for disband_org

        Disband org
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org(self):
        """Test case for get_org

        Get org info
        """
        query_string = [('org_id', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org_list(self):
        """Test case for get_org_list

        Get org info
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_verifier_password(self):
        """Test case for get_verifier_password

        Get password used by ID verifiers to login into voting machine
        """
        unknown_base_type = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/verifier_password',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_org(self):
        """Test case for update_org

        Update org info
        """
        unknown_base_type = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org',
            method='PUT',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
