num=int(input("enter the integer value:"))
rem=0
reversed_num=0
temp=num
while(num!=0):
    rem=num%10
    reversed_num=reversed_num*10+rem
    num=num//10
if(temp==reversed_num):
    print(temp,"is a palindrome number")
else:
    print(temp,"is not a palindrome number")