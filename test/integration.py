import unittest

import apitestcase


class TestGetMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration test on GET methods
    """
    def test_get(self):
        self.assertGet("http://httpbin.org/")

    def test_get_ip(self):
        self.assertGet("http://httpbin.org/ip", contains=["origin"])

    def test_get_ua(self):
        self.assertGet("http://httpbin.org/user-agent",
                       contains=["python-requests"])

    def test_get_headers(self):
        self.assertGet("http://httpbin.org/headers",
                       contains=["\"Host\": \"httpbin.org\"",
                             "X-Request-Id",
                             "Accept"])

    def test_get_args(self):
        payload = {"foo": "bar"}
        self.assertGet("http://httpbin.org/get", params=payload,
                       contains=["\"foo\": \"bar\""])


class TestPostMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration tests for POST methods
    """
    def test_post(self):
        self.assertPost("http://httpbin.org/post")

    def test_post_args(self):
        payload = {"foo": "bar"}
        self.assertPost("http://httpbin.org/post", contains=["bar"], params=payload)


class TestPutMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration tests for PUT method
    """
    def test_put(self):
        self.assertPut("http://httpbin.org/put")


class TestDeleteMethod(unittest.TestCase, apitestcase.TestCase):
    """
    Integration tests for DELETE method
    """
    def test_delete(self):
        self.assertDelete("http://httpbin.org/delete")
