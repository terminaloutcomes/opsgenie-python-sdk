# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class ListAlertNotesRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, limit=None, identifier=None, identifier_type='id', offset=None, direction='next', order='desc'):
        """
        ListAlertNotesRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'limit': 'int',
            'identifier': 'str',
            'identifier_type': 'str',
            'offset': 'str',
            'direction': 'str',
            'order': 'str'
        }

        self.attribute_map = {
            'limit': 'limit',
            'identifier': 'identifier',
            'identifier_type': 'identifierType',
            'offset': 'offset',
            'direction': 'direction',
            'order': 'order'
        }

        self._limit = limit
        self._identifier = identifier
        self._identifier_type = identifier_type
        self._offset = offset
        self._direction = direction
        self._order = order

    @property
    def limit(self):
        """
        Gets the limit of this ListAlertNotesRequest.
        Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100

        :return: The limit of this ListAlertNotesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this ListAlertNotesRequest.
        Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100

        :param limit: The limit of this ListAlertNotesRequest.
        :type: int
        """

        self._limit = limit

    @property
    def identifier(self):
        """
        Gets the identifier of this ListAlertNotesRequest.
        Identifier of alert which could be alert id, tiny id or alert alias

        :return: The identifier of this ListAlertNotesRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ListAlertNotesRequest.
        Identifier of alert which could be alert id, tiny id or alert alias

        :param identifier: The identifier of this ListAlertNotesRequest.
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")

        self._identifier = identifier

    @property
    def identifier_type(self):
        """
        Gets the identifier_type of this ListAlertNotesRequest.
        Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

        :return: The identifier_type of this ListAlertNotesRequest.
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """
        Sets the identifier_type of this ListAlertNotesRequest.
        Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

        :param identifier_type: The identifier_type of this ListAlertNotesRequest.
        :type: str
        """
        allowed_values = ["id", "alias", "tiny"]
        if identifier_type not in allowed_values:
            raise ValueError(
                "Invalid value for `identifier_type` ({0}), must be one of {1}"
                    .format(identifier_type, allowed_values)
            )

        self._identifier_type = identifier_type

    @property
    def offset(self):
        """
        Gets the offset of this ListAlertNotesRequest.
        Starting value of the offset property

        :return: The offset of this ListAlertNotesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this ListAlertNotesRequest.
        Starting value of the offset property

        :param offset: The offset of this ListAlertNotesRequest.
        :type: str
        """

        self._offset = offset

    @property
    def direction(self):
        """
        Gets the direction of this ListAlertNotesRequest.
        Page direction to apply for the given offset with 'next' and 'prev'

        :return: The direction of this ListAlertNotesRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this ListAlertNotesRequest.
        Page direction to apply for the given offset with 'next' and 'prev'

        :param direction: The direction of this ListAlertNotesRequest.
        :type: str
        """
        allowed_values = ["next", "prev"]
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                    .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def order(self):
        """
        Gets the order of this ListAlertNotesRequest.
        Sorting order of the result set

        :return: The order of this ListAlertNotesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this ListAlertNotesRequest.
        Sorting order of the result set

        :param order: The order of this ListAlertNotesRequest.
        :type: str
        """
        allowed_values = ["asc", "desc"]
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                    .format(order, allowed_values)
            )

        self._order = order

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
        if not isinstance(other, ListAlertNotesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
