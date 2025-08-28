
# Use sorted() with a lambda function to sort the list of strings ["apple", "banana", "cherry", "date"] by length.
s=["apple", "banana", "cherry", "date"]
res=sorted(s,key=lambda x:len(x))
print(res)