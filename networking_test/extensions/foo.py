# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc

from neutron_lib.api import extensions as api_extensions

from neutron.api.v2 import resource_helper

from networking_test.services.foo.common import constants


# Attribute Map
RESOURCE_ATTRIBUTE_MAP = {
    constants.FOOS: {
        'id': {'allow_post': False, 'allow_put': False,
               'is_visible': True},
        'name': {'allow_post': True, 'allow_put': True,
                 'validate': {'type:string': None},
                 'is_visible': True, 'default': ''},
        'bars': {'allow_post': True, 'allow_put': True,
                 'validate': {'type:values': None},
                 'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'validate': {'type:string': None},
                      'required_by_policy': True,
                      'is_visible': True}
    },
}


class Foo(api_extensions.ExtensionDescriptor):

    """API extenson for Foo support."""

    @classmethod
    def get_name(cls):
        return constants.FOO

    @classmethod
    def get_alias(cls):
        return constants.foo

    @classmethod
    def get_description(cls):
        return "Provide foos for everybody."

    @classmethod
    def get_updated(cls):
        return "2017-12-05T00:00:00-00:00"

    @classmethod
    def get_resources(cls):
        """Returns Ext Resources."""
        plural_mappings = resource_helper.build_plural_mappings(
            {}, RESOURCE_ATTRIBUTE_MAP)
        resources = resource_helper.build_resource_info(plural_mappings,
                                                        RESOURCE_ATTRIBUTE_MAP,
                                                        constants.FOO)

        return resources

    def get_extended_resources(self, version):
        if version == "2.0":
            return RESOURCE_ATTRIBUTE_MAP
        else:
            return {}


class FooPluginBase(object):

    def get_plugin_name(self):
        return constants.FOO

    def get_plugin_type(self):
        return constants.FOO

    def get_plugin_description(self):
        return 'Foo service plugin'

    @abc.abstractmethod
    def create_foo(self, context, foo):
        pass

    @abc.abstractmethod
    def get_foo(self, context, id, fields=None):
        pass

    @abc.abstractmethod
    def delete_foo(self, context, id):
        pass

    @abc.abstractmethod
    def get_foos(self, context, filters=None, fields=None):
        pass

    @abc.abstractmethod
    def update_foo(self, context, id, foo):
        pass
