# Use a lambda function with filter() to find all words in ["python", "java", "c++", "javascript"] that start with "j".
s=["python", "java", "c++", "javascript"]
r=list(filter(lambda x:x[0]=='j',s))
print(r)
# for i in s:
#     if i[0]=='j':
#         r.append(i)
# print(r)