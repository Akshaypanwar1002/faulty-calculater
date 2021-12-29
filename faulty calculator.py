print("This is a calculator :")
num1=int(input("enter first number :"))
print("enter your operator :")
opt=input()
num2 = int(input("enter your second number:"))
if opt=="+":
    if num1==56 and num2==9:
        print("77")
    else:
        print("sum of these number is :",num1+num2)
if opt=="-":
    if num1==200 and num2==90:
        print("156")
    else:
        print("sub of these number :",num1-num2)
if opt=="*":
    if num1==45 and num2==3:
        print("555")
    else:
        print("multiply of two number is :",num1*num2)
if opt=="/":
    if num1==56 and num2==6:
        print("Result==4")
    else:
        print("Divison of these number :",num1/num2)