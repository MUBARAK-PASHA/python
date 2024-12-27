n=int(input("Enter the integer:"))
if(n>=100 and n<=999) or (n>=-999 and n<=-100):
    print("three digit")
else:
    print("not a three digit")

Result="three digit" if(n>=100 and n<=999) or (n>=-999 and n<=-100) else "not a three digit"
print(Result)