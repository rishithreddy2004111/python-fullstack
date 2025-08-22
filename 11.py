s = {"John": 85, "Alice": 92, "Bob": 76, "Daisy": 89}
arr=[key for key,i in s.items() if i>80 ]
print(arr)