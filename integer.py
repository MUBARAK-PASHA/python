#Write a python programmeto cheque whether the user entered 2 integer values are equal or not
num1=int(input("Enter first integer:")) 
num2=int(input("Enter second integer"))
if(num1==num2):
    print("entered two integers are equal")
else:
    print("entered two integers are not equal")


#using ternary
Result= "entered two integers are equal" if(num1==num2)  else "entered two integers are not equal"
print(Result)