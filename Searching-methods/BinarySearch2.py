# recursive binary search.
def binarysearch(arr,start,end,n):
    while start<end:
        mid=(start+end)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]<n:
            return binarysearch(arr,mid+1,end,n)
        else:
            return binarysearch(arr,start,mid-1,n)
    return -1


if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8]
    n=6
    result=binarysearch(arr,0,len(arr)-1,n)
    if result != -1:
        print("Element is foud at index :",result)
    else:
        print("Element is not found.")