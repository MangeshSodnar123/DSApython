def selectionSort(arr):
    '''Time complexity is O(nxn), Because we need to visit all array elements to find one greatest element. And this need to be done for all n elements.'''
    sortedArr = []
    for i in range(len(arr)):
        smallestInd = findSmallest(arr)
        sortedArr.append(arr.pop(smallestInd))
    return sortedArr
        
def findSmallest(arr):
    smallest = arr[0]
    smallestInd = 0
    for i in range(len(arr)):
        if(arr[i]<smallest):
            smallest = arr[i]
            smallestInd = i
    return smallestInd
    
def binarySearch(arr,element):
    #declare left, right
    left = 0
    right = len(arr)-1
    #while left<=right
    while left <= right:
        mid=(left+right)//2
        if(arr[mid]==element):
            return mid
        elif(arr[mid]>element):
            right = mid-1
        elif(arr[mid]<element):
            left = mid + 1
    return -1

arr = [6,4,8,9,2,3,1]
sortedArr = selectionSort(arr)
print(sortedArr)
print(binarySearch(sortedArr,88))
