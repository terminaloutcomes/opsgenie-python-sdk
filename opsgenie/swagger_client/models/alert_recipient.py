# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class AlertRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, user=None, state=None, method=None, created_at=None, updated_at=None):
        """
        AlertRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'UserMeta',
            'state': 'str',
            'method': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime'
        }

        self.attribute_map = {
            'user': 'user',
            'state': 'state',
            'method': 'method',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt'
        }

        self._user = user
        self._state = state
        self._method = method
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def user(self):
        """
        Gets the user of this AlertRecipient.

        :return: The user of this AlertRecipient.
        :rtype: UserMeta
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this AlertRecipient.

        :param user: The user of this AlertRecipient.
        :type: UserMeta
        """

        self._user = user

    @property
    def state(self):
        """
        Gets the state of this AlertRecipient.

        :return: The state of this AlertRecipient.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AlertRecipient.

        :param state: The state of this AlertRecipient.
        :type: str
        """

        self._state = state

    @property
    def method(self):
        """
        Gets the method of this AlertRecipient.

        :return: The method of this AlertRecipient.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this AlertRecipient.

        :param method: The method of this AlertRecipient.
        :type: str
        """

        self._method = method

    @property
    def created_at(self):
        """
        Gets the created_at of this AlertRecipient.

        :return: The created_at of this AlertRecipient.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this AlertRecipient.

        :param created_at: The created_at of this AlertRecipient.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this AlertRecipient.

        :return: The updated_at of this AlertRecipient.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this AlertRecipient.

        :param updated_at: The updated_at of this AlertRecipient.
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AlertRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
