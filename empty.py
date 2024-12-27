Num = int(input("Enter the integer: "))
print("Entered integer is", "one digit" if -9 <= Num <= 9 else "two digit" if -99 <= Num <= 99 else "more than two digits")
