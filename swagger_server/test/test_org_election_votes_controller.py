# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestOrgElectionVotesController(BaseTestCase):
    """OrgElectionVotesController integration test stubs"""

    def test_upload_election_votes(self):
        """Test case for upload_election_votes

        Create/Update election results
        """
        body = None
        response = self.client.open(
            '/api/org/election/votes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
