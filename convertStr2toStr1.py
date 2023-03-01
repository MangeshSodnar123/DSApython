#convert str2 in str1
#declare a function(s1,s2,ind1,ind2):
def calculateOps(s1,s2,ind1,ind2):
    #the condition where s1 is ended and s2 is still remaining...then need to delete extra chars....so these delete operations are counted by following
    if(len(s1)==ind1):
        return len(s2)-ind2
        
    #if s2 reached to end then some chars need to be inserted....these operation count is given by following
    if(len(s2)==ind2):
        return len(s1)-ind1
        
    #but the s1[ind1]==s2[ind2] : then go ahead without changing anything . call function recursively by incresing ind1 and ind2 by 1 
    if (s1[ind1]==s2[ind2]):
        return calculateOps(s1,s2,ind1+1,ind2+1)

    else:
        deleteOp = 1 + calculateOps(s1,s2,ind1,ind2+1)
        insertOp = 1 + calculateOps(s1,s2,ind1+1,ind2)
        replaceOp = 1 + calculateOps(s1,s2,ind1+1,ind2+1)
        return min(deleteOp,insertOp,replaceOp)
        
str1 = 'table'
str2 = 'tbres'
print(calculateOps(str1,str2,0,0))
