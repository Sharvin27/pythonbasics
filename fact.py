def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
num=int(input("Enter a number"))
print("The factorial is",fact(num))
