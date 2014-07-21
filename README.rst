ApiTestCase
===========
An integration test suite for HTTP APIs.

.. image:: https://travis-ci.org/bramwelt/apitestcase.svg
    :target: https://travis-ci.org/bramwelt/apitestcase

Uses the requests_ library, and the python unittest_ library to build
integration tests for web apis.

The module itself is tested against httpbin_.

.. _requests: http://docs.python-requests.org/
.. _unittest: http://docs.python.org/3/library/unittest.html
.. _httpbin: http://httpbin.org/

Usage
-----

Simply add the ApiTestCase mixin to your class that extends python's
unittest.TestCase and use the assert methods to verify your API.

.. code-block:: python

    import unittest

    import apitestcase


    class MyApiIntegrationTest(unittest.TestCase, apitestcase.ApiTestCase):
        """
        Test my web API
        """

        def test_homepage(self):
            """
            Tests to make sure our homepage is up on staging and production.
            """

            expected_body = """
                Welcome to waldo's widgets!

                ACME Corp happy to provide you with top quality widgets.
                Order online now!
            """

            self.assertGet("http://example.com/", contains=[expected_body])

