# Use map() with a lambda function to convert the list [1, 2, 3, 4, 5] into their cubes.
arr=[1, 2, 3, 4, 5]
cubes=list(map(lambda x:x**3,arr))
print(cubes)