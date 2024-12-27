#write the python program to check whether the user enterred integer month number is valid or not valid
month=int(input("Enter any month number:"))
if(month>=1 and month<=12):
    print("valid month")
else:
    print("not valid month")