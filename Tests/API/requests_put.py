from Keywords.RequestModuleFunctions import ApiTestFunctions

cFunctions = ApiTestFunctions()

# Data that to be updated
payload = {
    "name": "morpheus",
    "job": "zion resident"
    }

# PUT method to update records
cFunctions.put_method("https://reqres.in/api/users/2", data=payload)
