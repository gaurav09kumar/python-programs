def linear_search(lst,target):
    for index in range(0,len(lst)):
        if lst[index] == target:
            return index
    return -1
    
target = 70
lst = [10,23,45,70,11]
print(linear_search(lst,target))
print(linear_search(lst,100))
