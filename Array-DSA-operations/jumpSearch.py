import math

def jumpsearch(arr,x,n):
    step=math.sqrt(n)
    prev=0
    while arr[int(min(step,n)-1)]<x:
        prev=step
        step += math.sqrt(n)
        if prev>n:
            return -1
        
    while arr[int(prev)]<x:
        prev += 1
        if prev == min(step,n):
            return -1
    if arr[int(prev)] == x:
        return int(prev)
    
    return -1



arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11 ,12 ,13 , 14, 15]
x=1
n=len(arr)
result=jumpsearch(arr,x,n)
if result != -1:
    print("Element is present at index :",result)
else:
    print("Element is not preseent.")
