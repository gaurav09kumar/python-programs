# Hashing
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0]*(max(n)+1) 
for i in range(0,len(hash_list)-1):
    if hash_list[n[i]] not in hash_list:
        hash_list.insert(hash_list[n[i]],1)
    else:
        hash_list[n[i]] = hash_list[n[i]] + 1

print("HASH LIST -- ", hash_list)

hash_map = {}
for j in range(0,len(m)):
    if m[j] <= max(n):
        hash_map[m[j]]=hash_list[m[j]] 
    else:
        hash_map[m[j]] = 0

print("HASH MAP -- ", hash_map)

"""
First For loop O(N)
Second Differnet Loop O(m)
Total Time Complexity - O(N) + O(m) -> 10 ^ 8 + 10 ^ 8
Space Complexity - HASH_LIST - O(11) --> Constant --> O(1)
"""

# Using Dict - using Hashing
hash_dict = dict()
for i in range(0,len(n)):
    hash_dict[n[i]] = hash_dict.get(n[i],0)+1
print("HASH MAP -- ", hash_dict)
num_of_occurences_of_n_in_m = dict()
for j in range(0,len(m)):
    num_of_occurences_of_n_in_m[m[j]] = hash_dict.get(m[j],0)
print(num_of_occurences_of_n_in_m)


# Character hashing:
s = "azyxyyzaaaa"
q = ["d","a","y","u"]
s_list = list(s)
char_occ_in_s = dict()
for i in range(0,len(s_list)):
    char_occ_in_s[s_list[i]] = char_occ_in_s.get(s_list[i],0)+1
print(char_occ_in_s)
char_occ_q_in_s = dict()
for j in range(0,len(q)):
    char_occ_q_in_s[q[j]] = char_occ_in_s.get(q[j],0)
print(char_occ_q_in_s)

"""
Constraints 'a' <= s[i] <= 'z'
ASCII CODE - 
97 - 122

We will create a list with length 0 to 123

s = "azyxyyzaaaa"
So at index of ascii(a) which is 97 make it 1

One optimization we can do is - as we know before 97 all the index data is waste

Length = 26
All with 0 = [0,0,0,0.........0]]
Hash_list = Index --> [0...........25]
for ch in s:
    ascii_val = ord(ch) # 97 
    index = ascii_val - 97
    Hash_list[index] += 1
O_P_DICT = {}
for ch in q:
    ascii_val = ord(ch)-97
    O_P_DICT[Hash_list[ascii_val]] = O_P_DICT.get(Hash_list[ascii_val],0)
    
If the list has upper and lower case characters then the O/P List take as 0 to 122
"""


