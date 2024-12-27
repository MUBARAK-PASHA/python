num=int(input("Enter the value of num:"))
print("Multiplication table of",num,":")
for num in range(1,num+1):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)