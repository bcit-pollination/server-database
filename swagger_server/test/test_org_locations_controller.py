# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body4 import Body4  # noqa: E501
from swagger_server.models.body5 import Body5  # noqa: E501
from swagger_server.models.body6 import Body6  # noqa: E501
from swagger_server.models.body7 import Body7  # noqa: E501
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgLocationsController(BaseTestCase):
    """OrgLocationsController integration test stubs"""

    def test_add_location(self):
        """Test case for add_location

        Add location
        """
        body = Body6()
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
        body = Body7()
        response = self.client.open(
            '/api/org/locations/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_locations_list(self):
        """Test case for get_locations_list

        Get all the org voting locations
        """
        body = Body4()
        response = self.client.open(
            '/api/org/locations/get/list',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_location(self):
        """Test case for update_location

        Update location
        """
        body = Body5()
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
