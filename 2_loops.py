n = int(input("Enter the number: "))
total = 0
while n > 0:
    i = n % 10       # Get the last digit
    total = total + i
    print(i)
    n = n // 10      # Remove the last digit (integer division)
print(total)
