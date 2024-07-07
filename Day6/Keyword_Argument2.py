def show(**num):
    for i, j in num.items():
        print(i, j)
show(n1=10, n2=20)

# Example

def show(**num):
    sum = 0
    for i, j in num.items():
        sum = sum+j
    print("Sum is ", sum)
show(n1=10, n2=20)