# From the list of dictionaries:Use a lambda function with max() to find the student with the highest score.
data = [{"name": "John", "score": 85},
        {"name": "Jane", "score": 92},
        {"name": "Dave", "score": 78}]
res=sorted(data,key=lambda x:x["score"],reverse=True)
print(res)