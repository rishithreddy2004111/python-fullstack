# From a list nums = [1, 2, 3, 4, 5], create a new list of tuples where each tuple contains the number and its cube. Example: [(1,1), (2,8), (3,27), ...].
n=[1,2,3,4,5]
arr=[(i,i**3) for i in n]
print(arr)
