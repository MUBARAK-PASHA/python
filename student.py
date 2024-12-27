name=str(input("student name:"))
sub1=int(input("subject 1 score:"))
sub2=int(input("subject 2 score:"))
sub3=int(input("subject 3 score:"))
if(sub1>=35 and sub2>=35 and sub3>=35):
    total=sub1+sub2+sub3
    average=(total)/3
    print(total)
    print(average)
    if(average>90):
         print("first class")
    elif(average>75):
        print("second class")
    elif(average>60):
        print("third class")
else:
    print("fail")


print("-----------------------------------------")
name=str(input("enter the student name:"))
sub1=int(input("enter the subject1 score:"))
sub2=int(input("enter the subject2 score:"))
sub3=int(input("enter the subject3 score:"))
print("--------------------------------------------")
print("Student Report Card:")
print("---------------------------------------------")
print("subject 1:",sub1)
print("subject 2:",sub2)
print("subject 3:",sub3)
print("---------------------------------------------")
if(sub1>=35 and sub2>=35 and sub3>=35):
    total=sub1+sub2+sub3
    print("Total:",total)
    average=(sub1+sub2+sub3)/3
    print("Average:",average)
    if(average>90):
        print("congratulations you have certified with first class")
    elif(average>75):
        print("congratulations you have certified with second class")
    elif(average>60):
        print("congratulations you have certified with thrid class")
else:
    print("you have failed")