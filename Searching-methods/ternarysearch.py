def ternarysearch(arr,start,end,x):
    while (end>=start):
        mid1=start+(end-start)//3
        mid2=end-(end-start)//3
        if arr[mid1]==x:
            return mid1
        if arr[mid2]==x:
            return mid2
        if arr[mid1]>x:
         return ternarysearch(arr,start,mid1-1,x)
        elif x>arr[mid2]:
           return ternarysearch(arr,mid2+1,end,x)
        else:
         return ternarysearch(arr,mid1+1,mid2-1,x)
    return-1
    

arr=[1,2,3,4,5,6,7,8,9,10]
x=6
result= ternarysearch(arr,0,len(arr)-1,x)

if result != -1:
    print("Element is present at index :",result)
else:
    print("Element is not present.")