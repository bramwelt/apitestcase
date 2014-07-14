ApiTestCase
===========
An integration test suite for testing HTTP APIs.

Uses the requests_ library, and the python unittest_ library to build
integration tests for web apis.

Usage
-----

Simply add the ApiTestCase mixin to your class that extends python's
unittest.TestCase and use the assert methods to verify your API.

.. code-block:: python

    import unittest

    import apitestcase


    class ApiTestCase(object):
        """
        Add assetion methods for HTTP Requests to TestCase
        """
        hosts = []

        def assert_get(endpoint="", status_code=200, body=""):
            """
            Asserts GET requests on a given endpoint
            """
            for host in hosts:
                response = requests.get(host+endpoint)
                self.assertEqual(resonse.status_code, status_code)
                self.assertContains(response.body, body)


    class MyApiIntegrationTest(unittest.TestCase, apitestcase.ApiTestCase):
        """
        Test my web API
        """
        hosts = ["http://staging.example.com", "http://example.com"]

        def test_homepage():
            """
            Tests to make sure our homepage is up on staging and production.
            """

            expected_body = """
                Welcome to waldo's widgets!

                ACME Corp happy to provide you with top quality widgets.
                Order online now!
            """

            self.assert_get("/", body=expected_body)

