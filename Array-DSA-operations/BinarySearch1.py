def binarysearch(arr,start,end,n):
    while start<end:
       mid=(start+end)//2
       if arr[mid]==n:
         return mid
       elif arr[mid]<n:
         start=mid+1
       else:
          end=mid-1
    return -1

if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8]
    n=int(input("Enter the no. : "))
    result=binarysearch(arr,0,len(arr)-1,n)
    if result != -1:
        print("Element is present at index :",result)
    else:
        print("Element is not present.")