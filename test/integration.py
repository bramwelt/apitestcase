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

    def test_GET_IP(self):
        self.assert_get(self.endpoint+"ip", body="origin")

    def test_GET_UA(self):
        self.assert_get(self.endpoint+"user-agent",
                        body="python-requests")
    
    def test_GET_headers(self):
        self.assert_get(self.endpoint+"headers",
                        body=["\"Host\": \"httpbin.org\"",
                              "X-Request-Id",
                              "Accept"])
    def test_GET_args(self):
        self.assert_get(self.endpoint+"get?foo=bar",
                        body="\"foo\": \"bar\"")
