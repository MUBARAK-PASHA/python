#write a pyhon program to check whether user entered integer is multiple of 3 and 5 or not using both of else if and terinary operator
num=int(input("Enter the integer:"))
if(num%3==0 and num%5==0):
    print("multiples of 3 and 5")
else:
    print("not a multiple of 3 and 5")

#using ternary operator
Result="multiples of 3 and 5" if(num%3==0 and num%5==0)  else  "not a multiple of 3 and 5"
print(Result)