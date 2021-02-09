# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.location import Location  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgLocationsController(BaseTestCase):
    """OrgLocationsController integration test stubs"""

    def test_add_location(self):
        """Test case for add_location

        Add location
        """
        body = Body()
        response = self.client.open(
            '/api/org/locations',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_location(self):
        """Test case for delete_location

        Delete location
        """
        headers = [('election_id', 56)]
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
        headers = [('election_id', 56)]
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
        body = Location()
        response = self.client.open(
            '/api/org/locations',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
