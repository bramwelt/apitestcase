import unittest

import apitestcase


class TestGetMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration test on GET methods
    """
    hosts = ["http://httpbin.org"]
    endpoint = "/"

    def test_get(self):
        self.assertGet(self.endpoint)

    def test_get_ip(self):
        self.assertGet(self.endpoint+"ip", body="origin")

    def test_get_ua(self):
        self.assertGet(self.endpoint+"user-agent",
                       body="python-requests")

    def test_get_headers(self):
        self.assertGet(self.endpoint+"headers",
                       body=["\"Host\": \"httpbin.org\"",
                             "X-Request-Id",
                             "Accept"])

    def test_get_args(self):
        self.assertGet(self.endpoint+"get?foo=bar",
                       body="\"foo\": \"bar\"")
