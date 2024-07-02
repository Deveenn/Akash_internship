# Python has two built-in methods that you can use on tuples.

# The count() method returns the number of times a specified value appears in the tuple.

mytuple = ("Python" , "Java" , "Php")

print(mytuple)

new = mytuple.count("Python")

print(new)

# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.

ans = mytuple.index("Php")
print(ans)