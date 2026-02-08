"""
Hollow Right Triangle
Problem Description:
You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', where the first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be right-aligned.
Input:
A single integer n, where 1 <= n <= 100.
Output:
A list of strings where each string represents a row in the hollow right-angled triangle.
Example:
Input: 4
Output: ['*', '**', '* *', '****']
Input: 5
Output: ['*', '**', '* *', '*  *', '*****']
"""
def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    return ["*"*x if x == 1 or x == n or x == 2 else "*" + " " * (x - 2) + "*" for x in range(1,n+1)]

print(generate_hollow_right_angled_triangle(6))
