# Generate a list of prime numbers between 1 and 100 using list comprehension.

arr=[i for i in range(2,101) if all(i%j!=0 for j in range(2,int(i**0.5)+1))]
print(arr)
