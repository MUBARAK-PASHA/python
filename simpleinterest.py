#write a python program to read the input for principle amount,rate of interest &time to calculate the simple interest
pa=int(input("Enter the principle amount:"))
roi=int(input("Enter the rate of interest :"))
ttc=int(input("Enter the time to calculate:"))
si=(pa*roi*ttc)/100
print(si)