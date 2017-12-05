Prerequisites
-------------

Before you install and configure the networking service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``networking_test`` database:

     .. code-block:: none

        CREATE DATABASE networking_test;

   * Grant proper access to the ``networking_test`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON networking_test.* TO 'networking_test'@'localhost' \
          IDENTIFIED BY 'NETWORKING_TEST_DBPASS';
        GRANT ALL PRIVILEGES ON networking_test.* TO 'networking_test'@'%' \
          IDENTIFIED BY 'NETWORKING_TEST_DBPASS';

     Replace ``NETWORKING_TEST_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``networking_test`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt networking_test

   * Add the ``admin`` role to the ``networking_test`` user:

     .. code-block:: console

        $ openstack role add --project service --user networking_test admin

   * Create the networking_test service entities:

     .. code-block:: console

        $ openstack service create --name networking_test --description "networking" networking

#. Create the networking service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        networking public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        networking internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        networking admin http://controller:XXXX/vY/%\(tenant_id\)s
