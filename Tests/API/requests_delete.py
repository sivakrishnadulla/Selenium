from Keywords.RequestModuleFunctions import ApiTestFunctions

cFunctions = ApiTestFunctions()

# DELETE method to remove any data
data = cFunctions.delete_method("https://reqres.in/api/users/3")
