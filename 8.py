arr=[[1,2],[3,4],[5,6]]
a=[arr[i][j] for i in range(len(arr)) for j in range(len(arr[0]))]
print(a)