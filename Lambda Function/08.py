# Use reduce() with a lambda function to find the product of numbers in [2, 3, 4, 5].
from functools import reduce
arr=[2, 3, 4, 5]
n=reduce(lambda x, y: x * y, arr)
print(n)