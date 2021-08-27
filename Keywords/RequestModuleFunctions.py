import requests
import json

class ApiTestFunctions:
    """
    Creating a class for requests module to prepare methods for all functions in requests with all properties

    """

    def __init__(self):
        """
        Instance is created for requests module that will be used as construtor in python
        """
        self.response = requests

    def get_url(self, url):
        """
        To get/open any api/url using get function in reqests module in python, using get function in requests module there
        are many properties like statuscode, text format of a data, headers of that API...
        :param url: URL of any api that to be tested
        :return: It will return data of a particular url
        """
        resp = self.response.get(url)
        print(resp.status_code)
        print(resp.text)
        print(resp.headers)


    def get_json(self, url):
        """
        Getting data from url and converting that into json format(key:value pairs)
        :param url: URL of any api that to be tested
        :return: It will return data from api into json format
        """
        resp_json = self.response.get(url)
        print(resp_json.json())

    def get_properties(self, url):
        """
        Getting data from url and getting some properties like encoding, cookies, content of that api, main url
        :param url: URL of any api that to be tested
        :return: It will return properties that are used in these method
        """
        res = self.response.get(url)
        print(res.encoding)
        print(res.cookies)
        print(res.content)
        print(res.url)

    def post_method(self, url, data):
        """
        In requests module post method is used to create a record or data and getting response whether that function is worked
        or not by checking status code
        :param url: URL of any api that to be tested
        :param data: Data that has to be created is loaded inside a variable and assigning that variable into args
        :return: It will return created data of that api in the form of json format and also content-type of that header
        """
        resp = self.response.post(url, data)
        print(resp.status_code)
        print(resp.json())
        print(resp.headers.get("Content-Type"))

    def put_method(self, url, data):
        """
        In requests module put method is used to update record. It can be existing record or create a new record based on the
        code developed by the developers
        :param url: URL of any api that to be tested
        :param data: Data that has to be updated
        :return: It will return updated data into json format and print statuscode of that function
        """
        res = self.response.put(url, data)
        print(res.status_code)
        print(res.json())

    def delete_method(self,url):
        """
        In requests module delete method is used to remoce/delete any api
        :param url: URL of any api that to be tested
        :return: It will return nothing but statuscode of that function
        """
        resp = self.response.delete(url)
        print(resp.status_code)

    def patch_method(self, url, data):
        """
        In requests module patch method also used to update records
        :param url: URL of any api that to be tested
        :param data: Data that has to be updated
        :return: It will return updated data and statuscode of its function
        """
        resp = self.response.patch(url, data)
        print(resp.status_code)
        print(resp.content)