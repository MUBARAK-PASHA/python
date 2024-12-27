#write the python program to check whether the user enterred integer is odd number or not
Num=int(input("Enter the integer:"))
if(Num%2!=0):
      print(Num,"is odd number")
else:
    print(Num,"is not an odd number")


    print("----------------------------------------")
num=int(input("enter the value:"))
print("even number from 1 to ",num,":")
for i in range(1,num+1):
    if(i%2!=0):
        print(i)


print("----------------------------------------")
num=int(input("enter the value:"))
print("even number from 1 to ",num,":")
for i in range(1,num+1,2):
    print(i)