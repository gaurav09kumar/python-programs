# Write a program to show such type of Layout of Number and Square
"""
    Number  Square
    1       1
    2       4
    3       9
    4       16
    5       25
"""

number = int(input('Enter the number : '))
print("Number\t\tSquare")
for item in range(1,number+1):
    print(f"{item}\t\t{item*item}")

# Algorithm
# Step1: Print "Number" & "Square" Having Two time Tab
# Step2: Print 1 and Multiplication of 1 By 1
# Step3: Print 2 and Multiplication of 2 By 2
# Step4: Print 3 and Multiplication of 3 By 3
# Step5: Concatenate Both As String Having Two Tab Space
# Step6: Follow Step6 for Step2 to Step5
