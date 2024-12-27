#write a python program to swap two numbers by taking th input from the user 
#without using third variable
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("Before swapping:")
print("num1=",num1)
print("num2=",num2)
num1,num2=num2,num1
print("after swappig:")
print("num1=",num1)
print("num2=",num2)
#with using third variable
temp=num1
num1=num2
num1=temp
print("after swappig:")
print("num1=",num1)
print("num2=",num2)
#using arithmatic operators
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("after swappig:")
print("num1=",num2)
print("num2=",num1)