import unittest

import apitestcase

class TestGETMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration test on GET methods
    """
    hosts = ["http://httpbin.org"]
    endpoint = "/"

    def test_GET(self):
        self.assert_get(self.endpoint)
