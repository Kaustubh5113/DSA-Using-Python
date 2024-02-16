def bubblesort(ar):
    x=len(ar)
    for i in range(x):
        swapped=False
        for j in range(0,x-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
                swapped=True
        if swapped == False:
            break
            
    
ar=[98,6,59,6,7,9]
print("Given Array :")
for i in range(len(ar)):
    print("%d" %ar[i] ,end=" " )
bubblesort(ar)
print("Sorted array:")
for i in range(len(ar)):
    print("%d" %ar[i] ,end=" ")
    