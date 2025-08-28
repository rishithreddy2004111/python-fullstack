# Given a dictionary students = {"John": 85, "Alice": 92, "Bob": 76, "Daisy": 89}, use list comprehension to get names of students who scored more than 80.
s = {"John": 85, "Alice": 92, "Bob": 76, "Daisy": 89}
arr=[key for key,i in s.items() if i>80 ]
print(arr)
