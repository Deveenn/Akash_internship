def show(*num):
    sum = 0
    for i in num:
        sum = sum+i
    print("Sum is ", sum)
show(10, 20)
show(10, 20, 30)