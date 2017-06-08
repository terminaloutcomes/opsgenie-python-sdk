# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class CreateAlertRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, user=None, note=None, source=None, message=None, alias=None, description=None, teams=None,
                 visible_to=None, actions=None, tags=None, details=None, entity=None, priority=None):
        """
        CreateAlertRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'str',
            'note': 'str',
            'source': 'str',
            'message': 'str',
            'alias': 'str',
            'description': 'str',
            'teams': 'list[TeamRecipient]',
            'visible_to': 'list[Recipient]',
            'actions': 'list[str]',
            'tags': 'list[str]',
            'details': 'dict(str, str)',
            'entity': 'str',
            'priority': 'str'
        }

        self.attribute_map = {
            'user': 'user',
            'note': 'note',
            'source': 'source',
            'message': 'message',
            'alias': 'alias',
            'description': 'description',
            'teams': 'teams',
            'visible_to': 'visibleTo',
            'actions': 'actions',
            'tags': 'tags',
            'details': 'details',
            'entity': 'entity',
            'priority': 'priority'
        }

        self._user = user
        self._note = note
        self._source = source
        self._message = message
        self._alias = alias
        self._description = description
        self._teams = teams
        self._visible_to = visible_to
        self._actions = actions
        self._tags = tags
        self._details = details
        self._entity = entity
        self._priority = priority

    @property
    def user(self):
        """
        Gets the user of this CreateAlertRequest.
        Display name of the request owner

        :return: The user of this CreateAlertRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this CreateAlertRequest.
        Display name of the request owner

        :param user: The user of this CreateAlertRequest.
        :type: str
        """

        self._user = user

    @property
    def note(self):
        """
        Gets the note of this CreateAlertRequest.
        Additional note that will be added while creating the alert

        :return: The note of this CreateAlertRequest.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this CreateAlertRequest.
        Additional note that will be added while creating the alert

        :param note: The note of this CreateAlertRequest.
        :type: str
        """

        self._note = note

    @property
    def source(self):
        """
        Gets the source of this CreateAlertRequest.
        Source field of the alert. Default value is IP address of the incoming request

        :return: The source of this CreateAlertRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateAlertRequest.
        Source field of the alert. Default value is IP address of the incoming request

        :param source: The source of this CreateAlertRequest.
        :type: str
        """

        self._source = source

    @property
    def message(self):
        """
        Gets the message of this CreateAlertRequest.
        Message of the alert

        :return: The message of this CreateAlertRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CreateAlertRequest.
        Message of the alert

        :param message: The message of this CreateAlertRequest.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def alias(self):
        """
        Gets the alias of this CreateAlertRequest.
        Client-defined identifier of the alert, that is also the key element of alert deduplication.

        :return: The alias of this CreateAlertRequest.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this CreateAlertRequest.
        Client-defined identifier of the alert, that is also the key element of alert deduplication.

        :param alias: The alias of this CreateAlertRequest.
        :type: str
        """

        self._alias = alias

    @property
    def description(self):
        """
        Gets the description of this CreateAlertRequest.
        Description field of the alert that is generally used to provide a detailed information about the alert.

        :return: The description of this CreateAlertRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAlertRequest.
        Description field of the alert that is generally used to provide a detailed information about the alert.

        :param description: The description of this CreateAlertRequest.
        :type: str
        """

        self._description = description

    @property
    def teams(self):
        """
        Gets the teams of this CreateAlertRequest.
        Teams that the alert will be routed to send notifications

        :return: The teams of this CreateAlertRequest.
        :rtype: list[TeamRecipient]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """
        Sets the teams of this CreateAlertRequest.
        Teams that the alert will be routed to send notifications

        :param teams: The teams of this CreateAlertRequest.
        :type: list[TeamRecipient]
        """

        self._teams = teams

    @property
    def visible_to(self):
        """
        Gets the visible_to of this CreateAlertRequest.
        Teams and users that the alert will become visible to without sending any notification

        :return: The visible_to of this CreateAlertRequest.
        :rtype: list[Recipient]
        """
        return self._visible_to

    @visible_to.setter
    def visible_to(self, visible_to):
        """
        Sets the visible_to of this CreateAlertRequest.
        Teams and users that the alert will become visible to without sending any notification

        :param visible_to: The visible_to of this CreateAlertRequest.
        :type: list[Recipient]
        """

        self._visible_to = visible_to

    @property
    def actions(self):
        """
        Gets the actions of this CreateAlertRequest.
        Custom actions that will be available for the alert

        :return: The actions of this CreateAlertRequest.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this CreateAlertRequest.
        Custom actions that will be available for the alert

        :param actions: The actions of this CreateAlertRequest.
        :type: list[str]
        """

        self._actions = actions

    @property
    def tags(self):
        """
        Gets the tags of this CreateAlertRequest.
        Tags of the alert

        :return: The tags of this CreateAlertRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CreateAlertRequest.
        Tags of the alert

        :param tags: The tags of this CreateAlertRequest.
        :type: list[str]
        """

        self._tags = tags

    @property
    def details(self):
        """
        Gets the details of this CreateAlertRequest.
        Map of key-value pairs to use as custom properties of the alert

        :return: The details of this CreateAlertRequest.
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this CreateAlertRequest.
        Map of key-value pairs to use as custom properties of the alert

        :param details: The details of this CreateAlertRequest.
        :type: dict(str, str)
        """

        self._details = details

    @property
    def entity(self):
        """
        Gets the entity of this CreateAlertRequest.
        Entity field of the alert that is generally used to specify which domain alert is related to

        :return: The entity of this CreateAlertRequest.
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this CreateAlertRequest.
        Entity field of the alert that is generally used to specify which domain alert is related to

        :param entity: The entity of this CreateAlertRequest.
        :type: str
        """

        self._entity = entity

    @property
    def priority(self):
        """
        Gets the priority of this CreateAlertRequest.
        Priority level of the alert

        :return: The priority of this CreateAlertRequest.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this CreateAlertRequest.
        Priority level of the alert

        :param priority: The priority of this CreateAlertRequest.
        :type: str
        """
        allowed_values = ["P1", "P2", "P3", "P4", "P5"]
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"
                    .format(priority, allowed_values)
            )

        self._priority = priority

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
        if not isinstance(other, CreateAlertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
