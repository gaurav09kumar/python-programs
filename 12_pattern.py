"""
Rectangle Pattern
Problem Description:

You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).



Input:

Two integers n and m, where 1 <= n, m <= 100.



Output:

A list of strings where each string represents a row of the rectangle pattern.



Example:

Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']
"""

def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Your code here
    return ["*" * m for row in range(n)]
    
print(generate_rectangle(3,4))
print(generate_rectangle(3,2))
print(generate_rectangle(5,5))
