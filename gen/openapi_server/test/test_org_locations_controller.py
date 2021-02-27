# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from openapi_server.models.location import Location  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrgLocationsController(BaseTestCase):
    """OrgLocationsController integration test stubs"""

    def test_add_location(self):
        """Test case for add_location

        Add location
        """
        unknown_base_type = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/locations',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_location(self):
        """Test case for delete_location

        Delete location
        """
        headers = { 
            'election_id': 56,
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/locations',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_locations_list(self):
        """Test case for get_locations_list

        Get all the org voting locations
        """
        headers = { 
            'Accept': 'application/json',
            'election_id': 56,
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/locations/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_location(self):
        """Test case for update_location

        Update location
        """
        location = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/locations',
            method='PUT',
            headers=headers,
            data=json.dumps(location),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
