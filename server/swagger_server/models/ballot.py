# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.question import Question  # noqa: F401,E501
from swagger_server import util


class Ballot(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, questions: List[Question]=None):  # noqa: E501
        """Ballot - a model defined in Swagger

        :param questions: The questions of this Ballot.  # noqa: E501
        :type questions: List[Question]
        """
        self.swagger_types = {
            'questions': List[Question]
        }

        self.attribute_map = {
            'questions': 'questions'
        }
        self._questions = questions

    @classmethod
    def from_dict(cls, dikt) -> 'Ballot':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ballot of this Ballot.  # noqa: E501
        :rtype: Ballot
        """
        return util.deserialize_model(dikt, cls)

    @property
    def questions(self) -> List[Question]:
        """Gets the questions of this Ballot.


        :return: The questions of this Ballot.
        :rtype: List[Question]
        """
        return self._questions

    @questions.setter
    def questions(self, questions: List[Question]):
        """Sets the questions of this Ballot.


        :param questions: The questions of this Ballot.
        :type questions: List[Question]
        """

        self._questions = questions
