# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.option_results import OptionResults
from openapi_server import util

from openapi_server.models.option_results import OptionResults  # noqa: E501

class QuestionResults(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, options_posed=None):  # noqa: E501
        """QuestionResults - a model defined in OpenAPI

        :param options_posed: The options_posed of this QuestionResults.  # noqa: E501
        :type options_posed: List[OptionResults]
        """
        self.openapi_types = {
            'options_posed': List[OptionResults]
        }

        self.attribute_map = {
            'options_posed': 'options_posed'
        }

        self._options_posed = options_posed

    @classmethod
    def from_dict(cls, dikt) -> 'QuestionResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The question_results of this QuestionResults.  # noqa: E501
        :rtype: QuestionResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def options_posed(self):
        """Gets the options_posed of this QuestionResults.

        The options given for this question  # noqa: E501

        :return: The options_posed of this QuestionResults.
        :rtype: List[OptionResults]
        """
        return self._options_posed

    @options_posed.setter
    def options_posed(self, options_posed):
        """Sets the options_posed of this QuestionResults.

        The options given for this question  # noqa: E501

        :param options_posed: The options_posed of this QuestionResults.
        :type options_posed: List[OptionResults]
        """

        self._options_posed = options_posed
