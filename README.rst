===============================
networking-test
===============================

Dummy extension for neutron

Neutron service plugin demonstration to show the pure mechanics of a neutron plugin.
It contains:

* API extension to terminate RESTFUL API calls like GET/POST/PUT/DELETE.

* Db migration scripts.

* Methods to terminate the API calls results in the database.

* (TODO)A small agent to demonstrate the rps side as well.

Free software: Apache license

Features
--------

* Neutron service plugin which makes it possible to manage your foos:

  - GET (list, show) foo/foos

  - POST (create) foo

  - PUT (update) foo

  - DELETE (surprisingly delete) foo

Usage
=====

Installation
------------

Neutron detects plugins by the entry_points from setup.cfg, so the plugin
installation is quite easy:

- Install the python package:
``sudo pip install .``

- Add foo to your neutron.conf service_plugins section:
``service_plugins = neutron.services.l3_router.l3_router_plugin.L3RouterPlugin,foo``

- Restart q-svc service:

  - ``sudo systemctl stop devstack@q-svc.service``

  - ``sudo systemctl start devstack@q-svc.service``

Usage
-----

TODO: client extension, or osclient extension.

- Fetch a token from keystone:
``TOKEN=$(openstack token issue -f value -c id)``

- Create a foo:
``curl -s -X POST -H "Accept: application/json" -H "Content-Type: application/json" -H "x-auth-token: $TOKEN" http://127.0.0.1:9696/v2.0/foos -d '{"foo": {"name": "apple", "fruit": "apple", "no_fruit": 1}}'``

- List the available foos:
``curl -s -X GET -H "Accept: application/json" -H "Content-Type: application/json" -H "x-auth-token: $TOKEN" http://127.0.0.1:9696/v2.0/foos``

- Show one foo with id:
``curl -s -X GET -H "Accept: application/json" -H "Content-Type: application/json" -H "x-auth-token: $TOKEN" http://127.0.0.1:9696/v2.0/foos/uuid``

- Update a foo:
``curl -s -X PUT -H "Accept: application/json" -H "Content-Type: application/json" -H "x-auth-token: $TOKEN" http://127.0.0.1:9696/v2.0/foos/uuid -d '{"foo": {"no_fruit": 4}}'``

- Delete a foo:
``curl -s -X DELETE -H "Accept: application/json" -H "Content-Type: application/json" -H "x-auth-token: $TOKEN" http://127.0.0.1:9696/v2.0/foos/uuid``
