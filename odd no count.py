num=int(input("Enter the integer:"))
count=0
for i in range(1,num+1):
    if(i%2!=0):
        count+=1
print("count of odd numbers from 1 to ",num,"is:",count)