def armstrong_number(num):
    # If dont want 2 while loops (Then do the count=len(str(num)))
    temp = num 
    arm_number = 0
    count = 0
    while(temp>0):
        digit = temp % 10
        temp = temp // 10
        count = count + 1
    temp = num
    while(temp>0):
        digit = temp % 10
        arm_number = arm_number + (digit**count)
        temp = temp // 10
    return arm_number==num
    
print(armstrong_number(153))
print(armstrong_number(1634))
