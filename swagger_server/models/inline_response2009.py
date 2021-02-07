# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.election import Election  # noqa: F401,E501
from swagger_server import util


class InlineResponse2009(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, elections: List[Election]=None):  # noqa: E501
        """InlineResponse2009 - a model defined in Swagger

        :param elections: The elections of this InlineResponse2009.  # noqa: E501
        :type elections: List[Election]
        """
        self.swagger_types = {
            'elections': List[Election]
        }

        self.attribute_map = {
            'elections': 'elections'
        }
        self._elections = elections

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2009':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_9 of this InlineResponse2009.  # noqa: E501
        :rtype: InlineResponse2009
        """
        return util.deserialize_model(dikt, cls)

    @property
    def elections(self) -> List[Election]:
        """Gets the elections of this InlineResponse2009.


        :return: The elections of this InlineResponse2009.
        :rtype: List[Election]
        """
        return self._elections

    @elections.setter
    def elections(self, elections: List[Election]):
        """Sets the elections of this InlineResponse2009.


        :param elections: The elections of this InlineResponse2009.
        :type elections: List[Election]
        """

        self._elections = elections
