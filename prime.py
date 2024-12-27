#write a python program to print prime numbers from 1 to n
num=int(input("enter any integer value:"))
for i in range(2,num+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)