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

from oslo_log import log as logging

from neutron_lib.plugins import directory

from neutron.services import service_base

from networking_test.db.foo import foo_db
from networking_test.services.foo.common import constants

LOG = logging.getLogger(__name__)


class FooPlugin(foo_db.FooMixin):
    """Implementation of the Neutron foo Service Plugin."""

    supported_extension_aliases = ["foo"]

    def __init__(self):
        super(FooPlugin, self).__init__()

    def _load_drivers(self):
        """Loads plugin-drivers specified in configuration."""
        self.drivers, self.default_provider = service_base.load_drivers(
            'FOO', self)

    @property
    def _core_plugin(self):
        return directory.get_plugin()

    def get_plugin_type(self):
        """Get type of the plugin."""
        return constants.FOO

    def get_plugin_description(self):
        """Get description of the plugin."""
        return constants.FOO_SERVICE_PLUGIN

    def create_foo(self, context, foo):
        LOG.debug("networking-test: create_foo")
        with context.session.begin(subtransactions=True):
            foo_instance = super(FooPlugin, self).create_foo(context, foo)
        return foo_instance

    def update_foo(self, context, foo_id, foo):
        LOG.debug("networking-test: update_foo")
        with context.session.begin(subtransactions=True):
            foo_instance = super(FooPlugin, self).update_foo(context, foo_id,
                                                             foo)
        return foo_instance

    def delete_foo(self, context, foo_id):
        LOG.debug("networking-test: delete_foo")
        with context.session.begin(subtransactions=True):
            super(FooPlugin, self).delete_foo(context, foo_id)
