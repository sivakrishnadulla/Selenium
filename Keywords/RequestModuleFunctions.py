import requests
import json

class ApiTestFunctions:
    """

    """

    def __init__(self):
        """

        """
        self.response = requests

    def get_url(self, url):
        """

        :return:
        """
        resp = self.response.get(url)
        print(resp.status_code)
        print(resp.text)
        print(resp.headers)


    def get_json(self, url):
        """

        :param url:
        :return:
        """
        resp_json = self.response.get(url)
        print(resp_json.json())

    def get_properties(self, url):
        """

        :param url:
        :return:
        """
        res = self.response.get(url)
        print(res.encoding)
        print(res.cookies)
        print(res.content)
        print(res.url)

    def post_method(self, url, data):
        """

        :param url:
        :param data:
        :return:
        """
        resp = self.response.post(url, data)
        print(resp.status_code)
        print(resp.json())
        print(resp.headers.get("Content-Type"))

    def put_method(self, url, data):
        """

        :param url:
        :param data:
        :return:
        """
        res = self.response.put(url, data)
        print(res.status_code)
        print(res.json())

    def delete_method(self,url):
        """

        :param url:
        :return:
        """
        resp = self.response.delete(url)
        print(resp.status_code)
