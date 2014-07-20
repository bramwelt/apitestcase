import requests


class TestCase(object):
    """
    Add assetion methods for HTTP Requests to TestCase
    """

    def assertGet(self, url="", status_code=200, contains=None):
        """
        Asserts GET requests on a given endpoint
        """
        if contains is None:
            cotains = []

        response = requests.get(url)
        self.assertEqual(response.status_code, status_code)
        if contains:
            for item in contains:
                self.assertIn(item, response.content)
