import sys

def SelectionSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    for i in range(len(arr)):
        print("%d" %arr[i],end=" , ")

arr=[22,4,8,7,20,50,700,25,20]
print("Given unsorted array :")
print(arr)
print("sorted array :")
SelectionSort(arr)


