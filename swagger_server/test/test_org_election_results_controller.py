# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.election_results import ElectionResults  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgElectionResultsController(BaseTestCase):
    """OrgElectionResultsController integration test stubs"""

    def test_get_election_results(self):
        """Test case for get_election_results

        Get election voting results
        """
        headers = [('election_id', 56)]
        response = self.client.open(
            '/api/org/elections/results',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
