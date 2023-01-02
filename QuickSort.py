a=[1,7,6,3,5,9,2,4]
def quicksort(arr):
    l=len(arr)
    if l<=1:
        return arr
    pivot=arr.pop()
    greater=[]
    smaller=[]
    for i in arr:
        if i>pivot:
            greater.append(i)
        if i<pivot:
            smaller.append(i)
    return quicksort(smaller)+[pivot]+quicksort(greater)
print(quicksort(a))