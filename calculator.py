print("select an operation to perform:")
print("1.add")
print("2.subtract")
print("3.multiflication")
print("4.division")
operation=int(input())
if operation==1:
    #code for add
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number"))
    print("the sum is:",(num1+num2))
elif operation==2:
    #code for sub
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number"))
    print("the result is:",(num1-num2))
elif operation==3:
    #code for mul
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number"))
    print("the result is:",(num1*num2))
elif operation==4:
    #code for division
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number"))
    print("the result is:",(int(num1/num2)))
else:
    print("invalid operation")