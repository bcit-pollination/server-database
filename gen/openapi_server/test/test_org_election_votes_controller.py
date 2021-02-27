# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrgElectionVotesController(BaseTestCase):
    """OrgElectionVotesController integration test stubs"""

    def test_upload_election_votes(self):
        """Test case for upload_election_votes

        Create/Update election results
        """
        unknown_base_type = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/election/votes',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
