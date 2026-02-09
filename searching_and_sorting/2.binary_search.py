def binary_search(sorted_list,target):
    start = 0
    end = len(sorted_list)-1
    while (start<=end):
        middle = (start+end)//2
        if sorted_list[middle]==target:
            return middle
        elif sorted_list[middle]>target:
            end = middle-1
        elif sorted_list[middle]<target:
            start = middle+1
    return -1

sorted_list = [10,23,35,45,50,70,85]
print(binary_search(sorted_list,200))
