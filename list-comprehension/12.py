# Create a list of Pythagorean triplets (a, b, c) where 1 <= a, b, c <= 20 and a² + b² = c².
# a=[]
# for i in range(1,21):
#     for j in range(1,21):
#         for k in range(1,21):
#             if i**2+j**2==k**2:
#                 a.append((i,j,k))
# print(a)
a=[(i,j,k) for i in range(1,21) for j in range(1,21) for k in range(1,21) if i**2+j**2==k**2]
print(a)
