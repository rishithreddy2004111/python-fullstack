# From a list words = ["madam", "python", "level", "world"], extract only the palindromes using list comprehension.
s=["madam", "python", "level", "world"]
s1=[i for i in s if i==i[::-1]]
print(s1)
