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


class Account(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Account - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'account_name': 'str',
            'account_email': 'str',
            'password': 'str',
            'newpassword': 'str',
            'fullname': 'str',
            'address': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'account_name': 'accountName',
            'account_email': 'accountEmail',
            'password': 'password',
            'newpassword': 'newpassword',
            'fullname': 'fullname',
            'address': 'address'
        }

        self._id = None
        self._account_name = None
        self._account_email = None
        self._password = None
        self._newpassword = None
        self._fullname = None
        self._address = None

    @property
    def id(self):
        """
        Gets the id of this Account.
        Unique identifier representing a specific account.

        :return: The id of this Account.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Account.
        Unique identifier representing a specific account.

        :param id: The id of this Account.
        :type: str
        """
        self._id = id

    @property
    def account_name(self):
        """
        Gets the account_name of this Account.
        account's name.

        :return: The account_name of this Account.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this Account.
        account's name.

        :param account_name: The account_name of this Account.
        :type: str
        """
        self._account_name = account_name

    @property
    def account_email(self):
        """
        Gets the account_email of this Account.
        Description of product.

        :return: The account_email of this Account.
        :rtype: str
        """
        return self._account_email

    @account_email.setter
    def account_email(self, account_email):
        """
        Sets the account_email of this Account.
        Description of product.

        :param account_email: The account_email of this Account.
        :type: str
        """
        self._account_email = account_email

    @property
    def password(self):
        """
        Gets the password of this Account.
        Display name of product.

        :return: The password of this Account.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Account.
        Display name of product.

        :param password: The password of this Account.
        :type: str
        """
        self._password = password

    @property
    def newpassword(self):
        """
        Gets the newpassword of this Account.
        new password.

        :return: The newpassword of this Account.
        :rtype: str
        """
        return self._newpassword

    @newpassword.setter
    def newpassword(self, newpassword):
        """
        Sets the newpassword of this Account.
        new password.

        :param newpassword: The newpassword of this Account.
        :type: str
        """
        self._newpassword = newpassword

    @property
    def fullname(self):
        """
        Gets the fullname of this Account.
        full name.

        :return: The fullname of this Account.
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """
        Sets the fullname of this Account.
        full name.

        :param fullname: The fullname of this Account.
        :type: str
        """
        self._fullname = fullname

    @property
    def address(self):
        """
        Gets the address of this Account.
        account address.

        :return: The address of this Account.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Account.
        account address.

        :param address: The address of this Account.
        :type: str
        """
        self._address = address

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
