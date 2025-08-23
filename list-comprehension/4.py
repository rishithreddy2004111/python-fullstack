# From a list nums = [5, 12, 7, 18, 3], create a new list that contains only numbers greater than 10.
arr=list(map(int,input().split()))
a=[i for i in arr if i>10]
print(a)
