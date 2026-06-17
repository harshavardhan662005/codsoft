num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
operation=input("enter operation(+,-,*,/):")
if operation =='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation =='*':
    result=num1*num2
elif operation =='/':
    if num2!=0:
        result=num1/num2
    else:
        result="error:division by zero"
else:
    result="invalid operation"
print("result:",result)