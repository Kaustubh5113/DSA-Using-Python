def sentinal(arr,ti,key):
    last=arr[ti-1]
    arr[ti-1]=key
    i=0
    while(arr[i]!=key):
        i+=1
    arr[ti-1]=last
    if ((i<ti-1) or (arr[ti-1]==key)):
        print("Element is present at index :",i)
    else:
        print("Element is not present.")
        
        

arr=[2,3,4,5,5,6,7,8]
ti=len(arr)
key=5
sentinal(arr,ti,key)