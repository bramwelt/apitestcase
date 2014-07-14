import unittest

import requests


class TestCase(object):
    """
    Add assetion methods for HTTP Requests to TestCase
    """
    hosts = []

    def assert_get(self, endpoint="", status_code=200, body=""):
        """
        Asserts GET requests on a given endpoint
        """
        for host in self.hosts:
            response = requests.get(host+endpoint)
            self.assertEqual(response.status_code, status_code)
            if body:
                self.assertContains(response.body, body)

