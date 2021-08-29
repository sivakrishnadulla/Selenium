from Keywords.RequestModuleFunctions import ApiTestFunctions
import json

cFunctions = ApiTestFunctions()

"""Creating a data in json file and opening the file with read mode"""
mydata = open("data.json", "r").read()

# POST method for creating a user
create_user = cFunctions.post_method(url="https://reqres.in/api/users", data=json.loads(mydata))
print(create_user.status_code)
#create_user_json = create_user.json()
#print(create_user_json["name"])

# POST method for registering user
""" loading data directly using a variable named as payload"""
payload_register = {
    "email": "eve.holt@reqres.in",
    "password": "python"
    }

register_email = cFunctions.post_method(url="https://reqres.in/api/register", data=payload_register)
print(register_email.url)
print(register_email.status_code)
print(register_email.content)

# POST method for unsucessful registration without using password
payload_unregister = {
    "email": "krishna@fife"
    }
unregister_email = cFunctions.post_method(url="https://reqres.in/api/register", data=payload_unregister)
print(unregister_email.status_code)
print(unregister_email.cookies)

#POST method for user login
payload_login = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }

login_user = cFunctions.post_method(url="https://reqres.in/api/login", data=payload_login)
print(login_user.headers)
print(login_user.text)
print(login_user.encoding)

#POST method for unsuccessful login
payload_unsuccess_login = {
    "email": "peter@klaven"
    }

unsuccess_login = cFunctions.post_method(url="https://reqres.in/api/login", data=payload_unsuccess_login)
print(unsuccess_login.status_code)
print(unsuccess_login.apparent_encoding)