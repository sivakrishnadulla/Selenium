from Keywords.RequestModuleFunctions import ApiTestFunctions

cFunction = ApiTestFunctions()
base_url = "https://reqres.in/api/"

# GET method for single user only
id_user2 = cFunction.get_url(url=base_url, params="users/2")
print(id_user2.content)

# GET method for single user not found
id_user23 = cFunction.get_url(url=base_url, params="users/23")
print(id_user23.status_code)

# GET method for list resource
unknown_user = cFunction.get_url(url=base_url, params="unknown")
print(unknown_user.text)
print(unknown_user.headers.get("Content-Type"))

# GET method for single resource
unknown_user2 = cFunction.get_url(url=base_url, params="unknown/2")
print(unknown_user2.cookies)

# GET method for single user not found
unknown_user23 = cFunction.get_url(url=base_url, params="unknown/23")
print(unknown_user23.encoding)

# GET method for delayed response
delay_time = cFunction.get_url(url=base_url, params="users?delay=5")
print(delay_time.status_code)

# GET method for list of users
# parameter = {"page:2"}   #we can define params as args.
json_resp = cFunction.get_url(url=base_url, params="users?page=2").json()
print(json_resp["support"]["url"])
print(json_resp['total_pages'])
# Intentionally trying for negative scenario
assert json_resp['total_pages'] == 2, "total pages count is not matching"
print(json_resp["data"][2]["first_name"])
assert json_resp["data"][2]["first_name"] != None

