from math import *
inp = 5689
num = inp
reverse = 0
count = 0
while(num>0):
    digit=num%10
    print(digit)
    count=count+1
    reverse=(reverse*10)+digit
    num=num//10 # TC O(log10(N))
print(count)
print(int(log10(inp)+1))
print(reverse)
print(inp==reverse) # Check if palindrome or not
