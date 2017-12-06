# All Rights Reserved 2017
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

import sqlalchemy as sa
from sqlalchemy.orm import exc

from oslo_log import log as logging
from oslo_utils import uuidutils

from neutron_lib.db import model_base

from neutron.db import common_db_mixin as base_db

from networking_test.extensions import foo
from networking_test.services.foo.common import constants
from networking_test.services.foo import exceptions as foo_exc

LOG = logging.getLogger(__name__)


class Foo(model_base.BASEV2, model_base.HasId, model_base.HasProject):
    """Represents a Foo resource."""
    __tablename__ = 'foos'

    name = sa.Column(sa.String(255))
    fruit = sa.Column(sa.String(255))
    no_fruit = sa.Column(sa.Integer)


class FooMixin(foo.FooPluginBase, base_db.CommonDbMixin):
    """Class FooMixin for handling foo resource"""
    foo_resource = foo

    def _make_foo_dict(self, foo, fields=None):
        res = {'id': foo['id'],
               'project_id': foo['project_id'],
               'name': foo['name'],
               'fruit': foo['fruit'],
               'no_fruit': foo['no_fruit']}
        return self._fields(res, fields)

    def _get_foo(self, context, id):
        try:
            return self._get_by_id(context, Foo, id)
        except exc.NoResultFound:
            raise foo_exc.FooNotFound(foo_id=id)

    def create_foo(self, context, foo):
        """Create a foo."""
        LOG.debug('create_foo() called, foo: %s', foo)
        to_create_foo = foo[constants.FOO_RESOURCE]
        project_id = to_create_foo['project_id']
        with context.session.begin(subtransactions=True):
            foo_db = Foo(
                id=to_create_foo.get('id', uuidutils.generate_uuid()),
                project_id=project_id,
                name=to_create_foo.get('name'),
                fruit=to_create_foo.get('fruit'),
                no_fruit=to_create_foo.get('no_fruit')
            )
            context.session.add(foo_db)
        return self._make_foo_dict(foo_db)

    def get_foo(self, context, id, fields=None):
        """Get foo."""
        LOG.debug('get_foo() called')
        foo_db = self._get_foo(context, id)
        return self._make_foo_dict(foo_db, fields)

    def get_foos(self, context, filters=None, fields=None):
        """Get foos."""
        LOG.debug('get_foos() called')
        return self._get_collection(context, Foo,
                                    self._make_foo_dict,
                                    filters=filters, fields=fields)

    def delete_foo(self, context, id):
        """Detele foo by id."""
        LOG.debug('delete_foo() called')
        with context.session.begin(subtransactions=True):
            count = context.session.query(Foo).filter_by(id=id).delete()
            if not count:
                raise foo_exc.FooNotFound(foo_id=id)

    def update_foo(self, context, id, foo):
        """Update foo."""
        LOG.debug('update_foo() called')
        foo_to_update = foo['foo']
        with context.session.begin(subtransactions=True):
            count = context.session.query(Foo).filter_by(id=id).update(
                foo_to_update)
            if not count:
                raise foo_exc.FooNotFound(foo_id=id)
        return self.get_foo(context, id)
