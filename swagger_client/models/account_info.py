# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class AccountInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AccountInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'account_name': 'str',
            'groups': 'list[UserGroupSO]',
            'services': 'list[ServicesSO]',
            'sites': 'list[SiteSO]'
        }

        self.attribute_map = {
            'id': 'id',
            'account_name': 'accountName',
            'groups': 'groups',
            'services': 'services',
            'sites': 'sites'
        }

        self._id = None
        self._account_name = None
        self._groups = None
        self._services = None
        self._sites = None

    @property
    def id(self):
        """
        Gets the id of this AccountInfo.


        :return: The id of this AccountInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccountInfo.


        :param id: The id of this AccountInfo.
        :type: str
        """
        self._id = id

    @property
    def account_name(self):
        """
        Gets the account_name of this AccountInfo.


        :return: The account_name of this AccountInfo.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this AccountInfo.


        :param account_name: The account_name of this AccountInfo.
        :type: str
        """
        self._account_name = account_name

    @property
    def groups(self):
        """
        Gets the groups of this AccountInfo.


        :return: The groups of this AccountInfo.
        :rtype: list[UserGroupSO]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this AccountInfo.


        :param groups: The groups of this AccountInfo.
        :type: list[UserGroupSO]
        """
        self._groups = groups

    @property
    def services(self):
        """
        Gets the services of this AccountInfo.


        :return: The services of this AccountInfo.
        :rtype: list[ServicesSO]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this AccountInfo.


        :param services: The services of this AccountInfo.
        :type: list[ServicesSO]
        """
        self._services = services

    @property
    def sites(self):
        """
        Gets the sites of this AccountInfo.


        :return: The sites of this AccountInfo.
        :rtype: list[SiteSO]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """
        Sets the sites of this AccountInfo.


        :param sites: The sites of this AccountInfo.
        :type: list[SiteSO]
        """
        self._sites = sites

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

