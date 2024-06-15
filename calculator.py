def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2
print("select operation/n"\
      "1.Add/n" \
      "2.Sub/n" \
      "3.multiply/n"\
      "4.divide/n"
                )
select = int(input("select from 1,2,3,4:"))
num1= int (input("enter the 1 no."))
num2 = int(input("select the 2 no."))

if select ==1:
    print(num1,"+",num2,"=",add(num1,num2))
if select ==2:
    print(num1,"-",num2,"=",sub(num1,num2))
if select ==3:
    print(num1,"*",num2,"=",multiply(num1,num2))
if select ==4:
    print(num1,"/",num2,"=",divide(num1,num2))
