#write a python program to print the summation of digits for user entered number
num=int(input("Enter the integer value:"))
sum_digits=0
rem=0
while(num!=0):
    rem=num%10
    sum_digits=sum_digits+rem
    num=num//10
print("summation of the digits is",sum_digits)