# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.election import Election  # noqa: E501
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from swagger_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgElectionsController(BaseTestCase):
    """OrgElectionsController integration test stubs"""

    def test_create_election(self):
        """Test case for create_election

        Create election
        """
        body = Election()
        response = self.client.open(
            '/api/org/elections',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_election(self):
        """Test case for delete_election

        Delete election
        """
        headers = [('election_id', 56)]
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
        headers = [('election_id', 56)]
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
        response = self.client.open(
            '/api/org/elections/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_election(self):
        """Test case for update_election

        update election
        """
        body = Election()
        response = self.client.open(
            '/api/org/elections',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
