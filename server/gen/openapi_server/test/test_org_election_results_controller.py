# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.election_results import ElectionResults  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrgElectionResultsController(BaseTestCase):
    """OrgElectionResultsController integration test stubs"""

    def test_get_election_results(self):
        """Test case for get_election_results

        Get election voting results
        """
        headers = { 
            'Accept': 'application/json',
            'election_id': 56,
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/elections/results',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
