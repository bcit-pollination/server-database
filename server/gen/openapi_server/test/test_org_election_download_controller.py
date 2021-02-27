# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response20011 import InlineResponse20011  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrgElectionDownloadController(BaseTestCase):
    """OrgElectionDownloadController integration test stubs"""

    def test_download_voting_package(self):
        """Test case for download_voting_package

        Download main RPI election package
        """
        headers = { 
            'Accept': 'application/json',
            'election_id': 56,
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/org/election/download',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
