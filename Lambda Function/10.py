# Use a lambda function with map() to convert the list of Celsius temperatures [0, 20, 30, 40] into Fahrenheit.
cel=[0, 20, 30, 40]
far=list(map(lambda x:(x*9/5)+32,cel))
print(far)