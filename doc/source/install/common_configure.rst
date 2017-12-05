2. Edit the ``/etc/networking_test/networking_test.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://networking_test:NETWORKING_TEST_DBPASS@controller/networking_test
