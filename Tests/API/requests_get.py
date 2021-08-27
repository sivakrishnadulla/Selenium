from Keywords.RequestModuleFunctions import ApiTestFunctions

cFunction = ApiTestFunctions()

# GET method for list of users
#parameter = {"page:2"}   #we can define params as args.
cFunction.get_properties("https://reqres.in/api/users?page=2")

#GET method for single user not found
cFunction.get_url("https://reqres.in/api/users/23")

# GET method for single user only
json_response = cFunction.get_json("https://reqres.in/api/users/2")
print(json_response["support"]["url"])
print(json_response['total_pages'])
#Intentionally trying for negative scenario
assert json_response['total_pages'] == 2, "total pages count is not matching"
print(json_response["data"][2]["first_name"])
assert json_response["data"][2]["first_name"] != None

# GET method for list resource
cFunction.get_url("https://reqres.in/api/unknown")

# GET method for single resource
cFunction.get_url("https://reqres.in/api/unknown/2")

# GET method for single user not found
cFunction.get_url("https://reqres.in/api/unknown/23")

#GET method for delayed response
cFunction.get_url("https://reqres.in/api/users?delay=3")
