Num=int(input("enter the integer: "))
if(Num>=-9 and Num<=9):
    print("Entered integer is one digit")
elif(Num>=-99 and Num<=99):
    print("Entered integer is two digit")
else:
    print("Entered integer is ")

#Another logic
Num=int(input("enter the integer: "))
if(Num>=10 and Num<=99) or (Num>=-99 and Num<=-10):
    print("its is two digit")
else:
    print("not two digit")