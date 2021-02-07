# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgRpisController(BaseTestCase):
    """OrgRpisController integration test stubs"""

    def test_add_rpi(self):
        """Test case for add_rpi

        Add voting machine
        """
        body = Body2()
        response = self.client.open(
            '/api/org/rpis',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assign_rpi(self):
        """Test case for assign_rpi

        Assign voting machine
        """
        body = None
        response = self.client.open(
            '/api/org/rpis',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_discard_rpi(self):
        """Test case for discard_rpi

        Discard RPI
        """
        body = Body3()
        response = self.client.open(
            '/api/org/rpis/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rpis(self):
        """Test case for get_rpis

        Get the voting machines belonging to this organization
        """
        query_string = [('org_id', 56)]
        response = self.client.open(
            '/api/org/rpis/get/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
