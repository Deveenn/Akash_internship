# Python has a set of built-in methods that you can use on list

#The append() method append(add) an element to the end of the list.
#Example1:

mylist = ["Java" , "Html" ,20]

print(mylist)

mylist.append("python")

print("This list is Append",mylist)

#The clear() method removes all the elements from a list.

mylist.clear()
print("This List is clear: ",mylist)

# The copy() method returns a copy of the specified list.

mylist2 = mylist.copy() 
print("This List is Copy: ",mylist2)


# The count() method returns the number of elements with the specified value.

mylist2 = mylist.count("Java") 
print("This List is counted: ",mylist2)

# The extend() method adds the specified list elements (or any iterable) to the end of the current list

mylist3 = ['php', 10]

mylist.extend(mylist3)
print("This List is extend",mylist)

# The index() method returns the position at the first occurrence of the specified value.
index = mylist.index(10)
print("This List give index number",index)

# The insert() method inserts the specified value at the specified position.

mylist.insert(1,'php')
print("This List is inserted",mylist)

# The pop() method removes the element at the specified position.
mylist.pop(1)
# It remove from Index Number
print("This will remove the value",mylist)


# The remove() method removes the first occurrence of the element with the specified value.
mylist.remove("php")
print("This removes java from List",mylist)

# The reverse() method reverses the sorting order of the elements.
mylist4= ["Java" , "Html" ,20]
mylist4.reverse()
print("This will reverse List",mylist4)

# The sort() method sorts the list ascending by default.
mylist5 =["Java" , "Html" ,'CSS']
mylist5.sort()
print("This List is Shorted",mylist5)

