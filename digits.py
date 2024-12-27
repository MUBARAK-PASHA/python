#write a python program to print the no of digits present in the user entered integer
num=int(input("Enter the integer value:"))
digitcount=0
while(num!=0):
    num=num//10
    digitcount=digitcount+1
print(digitcount,"digits")