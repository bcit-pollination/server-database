# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body8 import Body8  # noqa: E501
from swagger_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrgVerifiersController(BaseTestCase):
    """OrgVerifiersController integration test stubs"""

    def test_assign_verifier(self):
        """Test case for assign_verifier

        Assign verifier to location
        """
        body = None
        response = self.client.open(
            '/api/org/verifiers',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_org_verifiers(self):
        """Test case for get_org_verifiers

        Get all the verifiers for a given election
        """
        body = Body8()
        response = self.client.open(
            '/api/org/verifiers/list',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
