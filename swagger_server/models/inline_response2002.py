# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user_org import UserOrg  # noqa: F401,E501
from swagger_server import util


class InlineResponse2002(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, org: UserOrg=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger

        :param org: The org of this InlineResponse2002.  # noqa: E501
        :type org: UserOrg
        """
        self.swagger_types = {
            'org': UserOrg
        }

        self.attribute_map = {
            'org': 'org'
        }
        self._org = org

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002
        """
        return util.deserialize_model(dikt, cls)

    @property
    def org(self) -> UserOrg:
        """Gets the org of this InlineResponse2002.


        :return: The org of this InlineResponse2002.
        :rtype: UserOrg
        """
        return self._org

    @org.setter
    def org(self, org: UserOrg):
        """Sets the org of this InlineResponse2002.


        :param org: The org of this InlineResponse2002.
        :type org: UserOrg
        """

        self._org = org
