# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.election import Election  # noqa: E501
from openapi_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from openapi_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from openapi_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrgElectionsController(BaseTestCase):
    """OrgElectionsController integration test stubs"""

    def test_create_election(self):
        """Test case for create_election

        Create election
        """
        election = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/elections',
            method='POST',
            headers=headers,
            data=json.dumps(election),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_election(self):
        """Test case for delete_election

        Delete election
        """
        headers = { 
            'election_id': 56,
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/elections',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_election(self):
        """Test case for get_election

        Get election info
        """
        headers = { 
            'Accept': 'application/json',
            'election_id': 56,
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/elections',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_election_list(self):
        """Test case for get_election_list

        Get election info list
        """
        query_string = [('org_id', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/elections/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_election(self):
        """Test case for update_election

        update election
        """
        election = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/elections',
            method='PUT',
            headers=headers,
            data=json.dumps(election),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
