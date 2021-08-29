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
        pass

    def get_url(self, url, params):
        """
        To get/open any api/url using get function in reqests module in python, using get function in requests module there
        are many properties like statuscode, text format of a data, headers of that API...
        :param url: URL of any api that to be tested
        :param params: parameters for api url to get information
        :return: It will return the functionality of GET
        """
        try:
            response = requests.get(url, params)
            return response
        except json.decoder.JSONDecodeError:
            print("Something went wrong with json module")


    def post_method(self, url, data):
        """
        In requests module post method is used to create a record or data and getting response whether that function is worked
        or not by checking status code
        :param url: URL of any api that to be tested
        :param data: Data that has to be created is loaded inside a variable and assigning that variable into args
        :return: It will complete the functionality of post.
        """
        try:
            response = requests.post(url, data)
            return response
        except:
            print("Something went wrong")


    def put_method(self, url, data):
        """
        In requests module put method is used to update record. It can be existing record or create a new record based on the
        code developed by the developers
        :param url: URL of any api that to be tested
        :param data: Data that has to be updated
        :return: It will return the functinality of PUT
        """
        try:
            response = requests.put(url, data)
            return response
        except:
            print("Something went wrong")

    def delete_method(self, url):
        """
        In requests module delete method is used to remoce/delete any api
        :param url: URL of any api that to be tested
        :return: It will return the functionality of DELETE
        """
        try:
            response = requests.delete(url)
            return response
        except:
            print("Something went wrong")

    def patch_method(self, url, data):
        """
        In requests module patch method also used to update records
        :param url: URL of any api that to be tested
        :param data: Data that has to be updated
        :return: It will return the functionality of PATCH
        """
        try:
            response = requests.patch(url, data)
            return response
        except:
            print("Something went wrong")