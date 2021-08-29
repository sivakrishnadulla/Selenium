from Keywords.RequestModuleFunctions import ApiTestFunctions

cFunctions = ApiTestFunctions()

# Data that to be updated
payload = {
    "name": "morpheus",
    "job": "zion resident"
    }

# PUT method to update records
records = cFunctions.put_method(url="https://reqres.in/api/users/2", data=payload)
print(records.status_code)