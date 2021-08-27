from Keywords.RequestModuleFunctions import ApiTestFunctions

cFunctions = ApiTestFunctions()

payload = {
    "name": "morpheus",
    "job": "zion resident"
    }

# PUT method to update records
cFunctions.put_method("https://reqres.in/api/users/2", data=payload)
