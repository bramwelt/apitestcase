import requests


class TestCase(object):
    """
    Add assetion methods for HTTP Requests to TestCase
    """

    def assertRequest(self, method="GET", url="", status_code=200,
            contains=None, **kwargs):
        """
        Asserts requests on a given endpoint
        """
        if contains is None:
            cotains = []

        if method is "GET":
            request = requests.get
        elif method is "POST":
            request = requests.post
        elif method is "PUT":
            request = requests.put

        response = request(url, **kwargs)
        self.assertEqual(response.status_code, status_code)
        if contains:
            for item in contains:
                self.assertIn(item, response.content)

    def assertGet(self, *args, **kwargs):
        """
        Asserts GET requests on a URL
        """
        return self.assertRequest("GET", *args, **kwargs)

    def assertPost(self, *args, **kwargs):
        """
        Asserts POST requests on a URL
        """
        return self.assertRequest("POST", *args, **kwargs)

    def assertPut(self, *args, **kwargs):
        """
        Asserts PUT requests on a URL
        """
        return self.assertRequest("PUT", *args, **kwargs)
