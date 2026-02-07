"""
Hollow Square of side 'N'
Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).
Input Parameters:

n (int): The size of the square (number of rows and columns).

Output:
A list of strings where each string is a row of n characters, representing a hollow square.
Example:
Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
"""

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    x = []
    for i in range(n):
        y = ""
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                y = y+"*"
            else:
                y = y+" "
        x.append(y)
    return x
    
"""
Approach 2:
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")

Approach 3: with list comprehension
print(["*" * n if i == 0 or i == n-1 else "*" + " " * (n-2) + "*" for i in range(n)])
"""


    
