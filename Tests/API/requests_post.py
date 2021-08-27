from Keywords.RequestModuleFunctions import ApiTestFunctions
import json

cFunctions = ApiTestFunctions()

"""Creating a data in json file and opening the file with read mode"""
mydata = open("data.json", "r").read()
# POST method for creating a user
cFunctions.post_method("https://reqres.in/api/users", data=json.loads(mydata))

""" loading data directly using a variable named as payload"""
payload_register = {
    "email": "eve.holt@reqres.in",
    "password": "python"
    }
# POST method for registering user
cFunctions.post_method("https://reqres.in/api/register", data=payload_register)

payload_unregister = {
    "email": "krishna@fife"
    }
# POST method for unsucessful registration without using password
cFunctions.post_method("https://reqres.in/api/register", data=payload_unregister)

payload_login = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }

cFunctions.post_method("https://reqres.in/api/login", data=payload_login)

payload_unsuccess_login = {
    "email": "peter@klaven"
    }

cFunctions.post_method("https://reqres.in/api/login", data=payload_unsuccess_login)
