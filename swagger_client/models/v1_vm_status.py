# coding: utf-8

"""


    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1VMStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, node_name=None, migration_node_name=None, conditions=None, phase=None, graphics=None):
        """
        V1VMStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'node_name': 'str',
            'migration_node_name': 'str',
            'conditions': 'list[V1VMCondition]',
            'phase': 'str',
            'graphics': 'list[V1VMGraphics]'
        }

        self.attribute_map = {
            'node_name': 'nodeName',
            'migration_node_name': 'migrationNodeName',
            'conditions': 'conditions',
            'phase': 'phase',
            'graphics': 'graphics'
        }

        self._node_name = node_name
        self._migration_node_name = migration_node_name
        self._conditions = conditions
        self._phase = phase
        self._graphics = graphics

    @property
    def node_name(self):
        """
        Gets the node_name of this V1VMStatus.
        NodeName is the name where the VM is currently running.

        :return: The node_name of this V1VMStatus.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this V1VMStatus.
        NodeName is the name where the VM is currently running.

        :param node_name: The node_name of this V1VMStatus.
        :type: str
        """

        self._node_name = node_name

    @property
    def migration_node_name(self):
        """
        Gets the migration_node_name of this V1VMStatus.
        MigrationNodeName is the node where the VM is live migrating to.

        :return: The migration_node_name of this V1VMStatus.
        :rtype: str
        """
        return self._migration_node_name

    @migration_node_name.setter
    def migration_node_name(self, migration_node_name):
        """
        Sets the migration_node_name of this V1VMStatus.
        MigrationNodeName is the node where the VM is live migrating to.

        :param migration_node_name: The migration_node_name of this V1VMStatus.
        :type: str
        """

        self._migration_node_name = migration_node_name

    @property
    def conditions(self):
        """
        Gets the conditions of this V1VMStatus.
        Conditions are specific points in VM's pod runtime.

        :return: The conditions of this V1VMStatus.
        :rtype: list[V1VMCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1VMStatus.
        Conditions are specific points in VM's pod runtime.

        :param conditions: The conditions of this V1VMStatus.
        :type: list[V1VMCondition]
        """

        self._conditions = conditions

    @property
    def phase(self):
        """
        Gets the phase of this V1VMStatus.
        Phase is the status of the VM in kubernetes world. It is not the VM status, but partially correlates to it.

        :return: The phase of this V1VMStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1VMStatus.
        Phase is the status of the VM in kubernetes world. It is not the VM status, but partially correlates to it.

        :param phase: The phase of this V1VMStatus.
        :type: str
        """

        self._phase = phase

    @property
    def graphics(self):
        """
        Gets the graphics of this V1VMStatus.
        Graphics represent the details of available graphical consoles.

        :return: The graphics of this V1VMStatus.
        :rtype: list[V1VMGraphics]
        """
        return self._graphics

    @graphics.setter
    def graphics(self, graphics):
        """
        Sets the graphics of this V1VMStatus.
        Graphics represent the details of available graphical consoles.

        :param graphics: The graphics of this V1VMStatus.
        :type: list[V1VMGraphics]
        """

        self._graphics = graphics

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other