def insertionsort(arr,x):
    for i in range(1,x):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
          
arr=[54,6,7,3,9]
x=len(arr)
print("UnSorted Array : ")
for i in range(x):
    print("%d" %arr[i] , end=" ")
insertionsort(arr,x)
print("\n" "Sorted Array : ")
for i in range(x):
    print("%d" %arr[i] , end=" ")