def bubbleSort(custList,orderType):
    if orderType == "Ascending":
        for i in range(len(custList)-1):
            for j in range(len(custList)-1):
                if custList[j] > custList[j+1]:
                    custList[j],custList[j+1] = custList[j+1],custList[j]
                    
    else:
        for i in range(len(custList)-1):
            for j in range(len(custList)-1):
                if custList[j] < custList[j+1]:
                    custList[j],custList[j+1] = custList[j+1],custList[j]
                    
    return custList

def selectionSort(lst):
    for i in range(len(lst)):
        minIndex = i
        for j in range(i+1,len(lst)):
            if lst[minIndex] > lst[j]:
                minIndex = j
    
        lst[minIndex],lst[i] = lst[i],lst[minIndex]
        
    return lst

def bucketSort(customList):
    noOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    #create buckets
    for i in range(noOfBuckets):
        arr.append([])
    #loop all elements
    for j in customList:
        #find bucket index for each element of a list
        bucketIndex = math.ceil(j*noOfBuckets/maxValue)
        #append that element in appropriate bucket
        arr[bucketIndex-1].append(j)
    #run a loop through all buckets and get them sorted using external sort function.
    for k in range(noOfBuckets):
        arr[k] = selectionSort(arr[k])
    #run a loop for all elements and merge all buckets together.
    sortedList = []
    for i in range(noOfBuckets):
        for j in range(len(arr[i])):
            sortedList.append(arr[i][j])
            
    return sortedList

#6 Pivot sort
# helper function for pivot sort
def swap(lst,index1,index2):
    lst[index1],lst[index2] = lst[index2],lst[index1]
    return lst
    
def pivot(lst,pivotIndex,endIndex):
    startIndex = pivotIndex
    swapIndex = pivotIndex
    for i in range(pivotIndex+1,endIndex+1):
        if lst[i] < lst[pivotIndex]:
            swapIndex += 1
            lst = swap(lst,swapIndex,i)
    lst = swap(lst,pivotIndex,swapIndex)
    return swapIndex
    
def quickSortHelper(lst,left,right):
    if left < right:
        pivotIndex = pivot(lst,left,right)
        quickSortHelper(lst,left,pivotIndex-1)
        quickSortHelper(lst,pivotIndex+1,right)
    return lst
    
def quickSort(lst):
    return quickSortHelper(lst,0,len(lst)-1)
    
    
lst1 = [4,5,3,2,7,9,1,6,8,0]
#print(bucketSort(lst1))
print(quickSort(lst1))
print(lst1)
