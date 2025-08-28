# You are given a list of tuples:Use a lambda function with sorted() to sort by name alphabetically.
s=[("b", 25), ("d", 20), ("a", 23), ("c", 22)]
res=sorted(s,key=lambda x:x[0])
print(res)