num = int(input("Enter the integer number: "))

# Step 1: Check if the number is prime
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

# Step 2: Check if the number is a palindrome
original_num = num
reversed_num = 0
while original_num > 0:
    digit = original_num % 10
    reversed_num = reversed_num * 10 + digit
    original_num //= 10

# Step 3: Combine the results
if count == 2:  # If the number is prime
    if num == reversed_num:  # If the number is also a palindrome
        print(f"{num} is a prime palindrome number")
    else:
        print(f"{num} is a prime number but not a palindrome")
else:
    print(f"{num} is not a prime number")
