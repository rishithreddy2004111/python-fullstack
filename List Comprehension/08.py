# Flatten a 2D list matrix = [[1,2],[3,4],[5,6]] into a single list [1,2,3,4,5,6] using list comprehension. 
arr=[[1,2],[3,4],[5,6]]
a=[arr[i][j] for i in range(len(arr)) for j in range(len(arr[0]))]
print(a)
