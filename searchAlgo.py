def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
        
    return -1

def binarySearch(arr,value):
    start = 0
    end = len(arr) - 1
    mid = (start+end)//2
    
    while not(arr[mid] == value) and start <= end:
        if value > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end)//2
    if arr[mid] == value:
        return mid
    else:
        return -1
    
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
value = 77
print(binarySearch(arr,value))
