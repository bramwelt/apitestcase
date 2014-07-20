import requests


class TestCase(object):
    """
    Add assetion methods for HTTP Requests to TestCase
    """

    def assertGet(self, url="", status_code=200, body=""):
        """
        Asserts GET requests on a given endpoint
        """
        response = requests.get(url)
        self.assertEqual(response.status_code, status_code)
        for content in body:
            self.assertIn(content, response.content)
