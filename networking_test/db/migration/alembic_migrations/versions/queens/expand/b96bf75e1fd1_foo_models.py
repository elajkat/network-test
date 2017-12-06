# Copyright 2017 OpenStack Foundation
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
#

"""foo models

Revision ID: b96bf75e1fd1
Revises: e52555874f04
Create Date: 2017-12-06 09:38:32.444283

"""

# revision identifiers, used by Alembic.
revision = 'b96bf75e1fd1'
down_revision = 'e52555874f04'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('foos',
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=True),
                    sa.Column('project_id', sa.String(length=255),
                              nullable=True),
                    sa.Column('no_fruit', sa.Integer, nullable=False),
                    sa.Column('fruit', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
