# Use filter() with a lambda function to extract numbers greater than 50 from [10, 55, 32, 75, 90].
arr=[10, 55, 32, 75, 90]
n=list(filter(lambda x: x>50,arr))
print(n)