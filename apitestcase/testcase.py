import unittest

import requests


class TestCase(object):
    """
    Add assetion methods for HTTP Requests to TestCase
    """
    hosts = []

    def assertGet(self, endpoint="", status_code=200, body=""):
        """
        Asserts GET requests on a given endpoint
        """
        for host in self.hosts:
            response = requests.get(host+endpoint)
            self.assertEqual(response.status_code, status_code)
            if isinstance(body, str):
                self.assertIn(body, response.content)
            elif isinstance(body, list):
                for content in body:
                    self.assertIn(content, response.content)

