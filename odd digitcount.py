num=int(input("Enter the integer value:"))
odddigitcount=0
rem=0
while(num!=0):
    rem=num%10
    if(rem%2!=0):
        odddigitcount+=1
    num=num//10
print("no of odd digits are",odddigitcount)