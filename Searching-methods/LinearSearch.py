
# iterative Binary search
def search(arr,ti,x):
    
    for i in range(0,ti):
        if(arr[i]==x):
            return i
        
    return -1

if __name__ =="__main__":
    arr=[2,3,4,5,6,7,8,9]
    x=5
    ti=len(arr)
    
    result=search(arr,ti,x)
    if (result==-1):
        print("Element is not present in array")
    else:
        print("Element is present at index:",result)