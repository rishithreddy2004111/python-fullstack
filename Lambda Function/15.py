# You have two lists:Use a lambda function with map() to add the corresponding elements of the two lists.
a = [1, 2, 3]
b = [4, 5, 6]
res=list(map(lambda x,y:x+y,a,b))
print(res)