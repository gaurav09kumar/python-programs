# How to create a frequency dict 
nums = [5,6,7,8,9,10,6,7]
empty_dict = {}
for i in range(0,len(nums)): # For N times loop will run
    if nums[i] in empty_dict: # O(1) to check if a key is available in the dict
        empty_dict[i] = empty_dict.get(i,0) + 1
    else:
        empty_dict[nums[i]] = 1
print(empty_dict)

# Let me know how many times 10 has come
print(empty_dict.get(10))

# Space Complexity - In worst case O(n) based on the number of items

# Approach 2
hash_map = {}
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)

# Time Complexity O(N)
# Space Complexity 

