def bubble_sort(lst):
    # Your code goes here
    if len(lst) <= 1:  # Handle empty/single element
        return lst
    start = 0
    end = len(lst)-1
    while(start<end):
        for i in range(start,end):
            if lst[i]>lst[i+1]:
                temp=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=temp
        end=end-1
    return lst

print(bubble_sort([12,25,11,34,90,22]))
        
