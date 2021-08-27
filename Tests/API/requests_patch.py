from Keywords.RequestModuleFunctions import ApiTestFunctions

cFunctions = ApiTestFunctions()

# Data to be updated
payload = {
    "name": "Rahul",
    "job": "Team Lead"
    }

# PATCH method to update data
cFunctions.patch_method("https://reqres.in/api/users/2", data=payload)
