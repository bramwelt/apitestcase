import unittest

import apitestcase


class TestGetMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration test on GET methods
    """
    def test_get(self):
        self.assertGet("http://httpbin.org/")

    def test_get_ip(self):
        self.assertGet("http://httpbin.org/ip", body="origin")

    def test_get_ua(self):
        self.assertGet("http://httpbin.org/user-agent",
                       body="python-requests")

    def test_get_headers(self):
        self.assertGet("http://httpbin.org/headers",
                       body=["\"Host\": \"httpbin.org\"",
                             "X-Request-Id",
                             "Accept"])

    def test_get_args(self):
        self.assertGet("http://httpbin.org/get?foo=bar",
                       body="\"foo\": \"bar\"")
