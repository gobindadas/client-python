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


class V1Graphics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, auto_port=None, default_mode=None, listen=None, passwd_valid_to=None, port=None, tls_port=None, type=None):
        """
        V1Graphics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'auto_port': 'str',
            'default_mode': 'str',
            'listen': 'V1Listen',
            'passwd_valid_to': 'str',
            'port': 'int',
            'tls_port': 'int',
            'type': 'str'
        }

        self.attribute_map = {
            'auto_port': 'autoPort',
            'default_mode': 'defaultMode',
            'listen': 'listen',
            'passwd_valid_to': 'passwdValidTo',
            'port': 'port',
            'tls_port': 'tlsPort',
            'type': 'type'
        }

        self._auto_port = auto_port
        self._default_mode = default_mode
        self._listen = listen
        self._passwd_valid_to = passwd_valid_to
        self._port = port
        self._tls_port = tls_port
        self._type = type

    @property
    def auto_port(self):
        """
        Gets the auto_port of this V1Graphics.


        :return: The auto_port of this V1Graphics.
        :rtype: str
        """
        return self._auto_port

    @auto_port.setter
    def auto_port(self, auto_port):
        """
        Sets the auto_port of this V1Graphics.


        :param auto_port: The auto_port of this V1Graphics.
        :type: str
        """

        self._auto_port = auto_port

    @property
    def default_mode(self):
        """
        Gets the default_mode of this V1Graphics.


        :return: The default_mode of this V1Graphics.
        :rtype: str
        """
        return self._default_mode

    @default_mode.setter
    def default_mode(self, default_mode):
        """
        Sets the default_mode of this V1Graphics.


        :param default_mode: The default_mode of this V1Graphics.
        :type: str
        """

        self._default_mode = default_mode

    @property
    def listen(self):
        """
        Gets the listen of this V1Graphics.


        :return: The listen of this V1Graphics.
        :rtype: V1Listen
        """
        return self._listen

    @listen.setter
    def listen(self, listen):
        """
        Sets the listen of this V1Graphics.


        :param listen: The listen of this V1Graphics.
        :type: V1Listen
        """

        self._listen = listen

    @property
    def passwd_valid_to(self):
        """
        Gets the passwd_valid_to of this V1Graphics.


        :return: The passwd_valid_to of this V1Graphics.
        :rtype: str
        """
        return self._passwd_valid_to

    @passwd_valid_to.setter
    def passwd_valid_to(self, passwd_valid_to):
        """
        Sets the passwd_valid_to of this V1Graphics.


        :param passwd_valid_to: The passwd_valid_to of this V1Graphics.
        :type: str
        """

        self._passwd_valid_to = passwd_valid_to

    @property
    def port(self):
        """
        Gets the port of this V1Graphics.


        :return: The port of this V1Graphics.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1Graphics.


        :param port: The port of this V1Graphics.
        :type: int
        """

        self._port = port

    @property
    def tls_port(self):
        """
        Gets the tls_port of this V1Graphics.


        :return: The tls_port of this V1Graphics.
        :rtype: int
        """
        return self._tls_port

    @tls_port.setter
    def tls_port(self, tls_port):
        """
        Sets the tls_port of this V1Graphics.


        :param tls_port: The tls_port of this V1Graphics.
        :type: int
        """

        self._tls_port = tls_port

    @property
    def type(self):
        """
        Gets the type of this V1Graphics.


        :return: The type of this V1Graphics.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Graphics.


        :param type: The type of this V1Graphics.
        :type: str
        """

        self._type = type

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