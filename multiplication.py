#write a python program to write a multiplication table 
num=int(input("Enter the value of num:"))
print("Multiplication table of",num,":")
for i in range(1,11):
    print(num,"x",i,"=",num*i)