num = int(input("Enter a positive number: "))

if num < 0:
    print("Please enter a positive number")
else:
    result = 1
    for i in range(1, num + 1):
        result = result * i
    print(f"The factorial of {num} is {result}")
