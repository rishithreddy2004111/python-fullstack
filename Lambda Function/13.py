# Given a list ["123", "456", "789"], use a lambda function with map() to convert it into integers.
arr=["123", "456", "789"]
res=list(map(lambda x:int(x),arr))
print(res)