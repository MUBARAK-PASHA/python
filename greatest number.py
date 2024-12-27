num1=int(input("Enter first integer:")) 
num2=int(input("Enter second integer"))
if(num1>num2):
    print(num1,"is greater value")
else:
    print(num2,"is not greater value")

#using ternary 
Result= num1,"is greater value" if(num1>num2) else num2,"is not greater value"
print(Result)