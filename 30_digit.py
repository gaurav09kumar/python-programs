from math import *
inp = 5689
num = inp
count = 0
while(num>0):
    digit=num%10
    print(digit)
    count=count+1
    num=num//10 # TC O(log10(N))
print(count)
print(int(log10(inp)+1))
