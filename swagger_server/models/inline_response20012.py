# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.election_results import ElectionResults  # noqa: F401,E501
from swagger_server import util


class InlineResponse20012(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, elections: List[ElectionResults]=None):  # noqa: E501
        """InlineResponse20012 - a model defined in Swagger

        :param elections: The elections of this InlineResponse20012.  # noqa: E501
        :type elections: List[ElectionResults]
        """
        self.swagger_types = {
            'elections': List[ElectionResults]
        }

        self.attribute_map = {
            'elections': 'elections'
        }
        self._elections = elections

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20012':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_12 of this InlineResponse20012.  # noqa: E501
        :rtype: InlineResponse20012
        """
        return util.deserialize_model(dikt, cls)

    @property
    def elections(self) -> List[ElectionResults]:
        """Gets the elections of this InlineResponse20012.


        :return: The elections of this InlineResponse20012.
        :rtype: List[ElectionResults]
        """
        return self._elections

    @elections.setter
    def elections(self, elections: List[ElectionResults]):
        """Sets the elections of this InlineResponse20012.


        :param elections: The elections of this InlineResponse20012.
        :type elections: List[ElectionResults]
        """

        self._elections = elections
