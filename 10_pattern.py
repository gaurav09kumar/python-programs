"""
Problem Description: 
You are given an integer n. 
Your task is to return a square pattern of size n x n made up of the character '*', 
represented as a list of strings

Input Parameters:

n (int): The size of the square (number of rows and columns).



Output:

A list of strings where each string is a row of n characters.



Example:

Input: 3
Output: ['***', '***', '***']
 
Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']

"""

def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    return ["*"*n for i in range(n)]

print(generate_square(5))
print(generate_square(3))
print(generate_square(1))
