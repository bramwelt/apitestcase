import unittest

import apitestcase


class TestGetMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration test on GET methods
    """
    hosts = ["http://httpbin.org"]

    def test_get(self):
        self.assertGet("/")

    def test_get_ip(self):
        self.assertGet("/ip", body="origin")

    def test_get_ua(self):
        self.assertGet("/user-agent",
                       body="python-requests")

    def test_get_headers(self):
        self.assertGet("/headers",
                       body=["\"Host\": \"httpbin.org\"",
                             "X-Request-Id",
                             "Accept"])

    def test_get_args(self):
        self.assertGet("/get?foo=bar",
                       body="\"foo\": \"bar\"")
