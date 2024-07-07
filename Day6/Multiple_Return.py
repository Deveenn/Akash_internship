# No argument, Return type
def sum():
    n1 = 10
    n2 = 20
    ans = n1+n2
    return ans, n1, n2
ans, n1, n2 = sum()
print("n1 is ", n1)
print("n2 is ", n2)
print("Sum is ", ans)   