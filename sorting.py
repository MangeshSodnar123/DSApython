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


lst = [4,5,3,2,7,9,1,6,8,0]
print(bubbleSort(lst,"Descending"))
