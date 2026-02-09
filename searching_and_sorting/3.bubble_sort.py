def bubble_sort(arr):
    start = 0
    end = len(arr)-1
    while(start!=end):
        for i in range(start,end):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
        end=end-1
    return arr

print(bubble_sort([12,25,11,34,90,22]))
        
