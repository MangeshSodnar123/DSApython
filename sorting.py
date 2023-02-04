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


lst = [4,5,3,2,7,9,1,6,8,0]
print(bubbleSort(lst,"Descending"))
