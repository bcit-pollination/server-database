# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.election_results import ElectionResults  # noqa: E501
from swagger_server.models.inline_response20010 import InlineResponse20010  # noqa: E501
from swagger_server.test import BaseTestCase


class TestElectionsResultsPublicController(BaseTestCase):
    """ElectionsResultsPublicController integration test stubs"""

    def test_get_public_election_result(self):
        """Test case for get_public_election_result

        Get public elections
        """
        query_string = [('election_id', 56)]
        response = self.client.open(
            '/api/org/elections/public/get',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_public_election_result_list(self):
        """Test case for get_public_election_result_list

        Get public elections
        """
        query_string = [('page', 56),
                        ('elections_per_page', 56)]
        response = self.client.open(
            '/api/org/elections/public/get/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
