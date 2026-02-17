# Print factors / Divisors
"""
10 {1 2 5 10}
15 {1 3 5}
25 {1 5 25}
7 {1 7}
19 {1 9}
"""
def factors(num):
    ans = [] # Space Complexity - O(k) k would be the total number of factors
    for i in range(1,num+1): # Time Complexity - O(N)
        if  num % i == 0: # O(1) So ignore
            ans.append(i) # O(1) So ignore
    return ans

print(factors(10))
print(factors(15))
print(factors(25))

def factors2(num):
    ans = [] # Space Complexity - O(k) k would be the total number of factors
    for i in range(1,num//2+1): # Time Complexity O(N/2) -> O(N * 1/2) -> Almost equal to O(N)
        if  num % i == 0: # O(1) So ignore
            ans.append(i) # O(1) So ignore
    ans.append(num) # O(1) So ignore
    return ans

print(factors2(10))
print(factors2(15))
print(factors2(25))

# optimal
def factors3(num):
    ans = [] # Space Complexity - O(k) k would be the total number of factors
    for i in range(1,int((num)**(1/2))+1): # Time Complexity O(N/2) -> O(Square root of N)
        if num % i == 0: # O(1) So ignore
           ans.append(i) # O(1) So ignore
           if num // i != i:
               ans.append(num//i) # O(1) So ignore
        ans.sort() # O(Nlogn)
    return ans

print(factors3(10))
print(factors3(15))
print(factors3(25))

# O(Square root of N) + O(Nlogn)
# Space Complexity O(k) k is the number of factors
