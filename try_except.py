x=input("Enter a number 1:")
y=input("Enter a number 2:")
try:
    print("The sum is :",int(x)+int(y))
except Exception as e:
    print(e)
finally:
    print("The line is very important")
