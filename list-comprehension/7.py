s="List comprehensions are powerful"
s1=s.split()
arr=[i for i in s1 if len(i)>=5]
print(arr)