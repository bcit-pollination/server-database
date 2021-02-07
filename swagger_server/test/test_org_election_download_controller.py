# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response20013 import InlineResponse20013  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgElectionDownloadController(BaseTestCase):
    """OrgElectionDownloadController integration test stubs"""

    def test_download_voting_package(self):
        """Test case for download_voting_package

        Download main RPI election package
        """
        body = None
        response = self.client.open(
            '/api/org/election/download',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
