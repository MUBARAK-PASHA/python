#write a python progrsm to print the number of even digits present in the user entered integer
num=int(input("Enter the integer value:"))
evendigitcount=0
rem=0
while(num!=0):
    rem=num%10
    if(rem%2==0):
        evendigitcount+=1
    num=num//10
print("no of even digits are",evendigitcount)