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

from networking_test.extensions import foo

LOG = logging.getLogger(__name__)


class FooPlugin(foo.FooPluginBase):
    """Implementation of the Neutron foo Service Plugin."""

    supported_extension_aliases = ["foo"]

    def __init__(self):
        pass

    def get_foos(self, context, filters=None, fields=None):
        LOG.debug("networking-test: get_foos")
        return ()

    def get_foo(self, context, service_id, fields=None):
        LOG.debug("networking-test: get_foo")

    def create_foo(self, context, service):
        LOG.debug("networking-test: create_foo")

    def update_foo(self, context, service_id, service):
        LOG.debug("networking-test: update_foo")

    def delete_foo(self, context, service_id):
        LOG.debug("networking-test: delete_foo")
