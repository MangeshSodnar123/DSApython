# def countDown(num):
    
#     print(num)
    
#     #base Condition.
#     if(num<=0):
#         return
#     #Recursive condition.
#     else:
#         countDown(num-1)
        
# countDown(20)

# #Write out a code for sum function that gives sum of all elements in the array.
# def sumOfArray(arr):
#     #base Condition
#     if len(arr)==1:
#         return arr[0]
#     #recursive condition
#     return arr.pop(0) + sumOfArray(arr)
    
# print(sumOfArray([1,2,3,4]))

# #Write a recursive function to count the number of items in a list
# def numberOfItems(arr):
#     #base condition
#     if len(arr)==1:
#         return 1
#     #recursive condition
#     arr.pop()
#     return 1 + numberOfItems(arr)
    
# print(numberOfItems([1,2,3,4,4,53,2,6]))

# # #binary search using the recursion
# def binarySearchRec(arr,left,right,ele):
#     #base condition
#     if(left<=right):
#         mid = (left+right)//2
#         # print(mid)
#         if(arr[mid]==ele):
#             return mid
#         #recursive condition
#         elif(arr[mid]>ele):
#             return binarySearchRec(arr,left,mid-1,ele)
#         else:
#             return binarySearchRec(arr,mid+1,right,ele)
            
#     else:
#         #if element is not present in the arr.
#         return -1
#     #return -1

# arr = [0,1,2,3,4,5,6,7,8,9,10]
# left = 0
# right = len(arr)-1
# ele = 100

# print(binarySearchRec(arr,left,right,ele))


# #find the maximum number in the list
# def findMax(arr):
#     #base condition
#     #recursive condition
#     maxi = 


##quickSort algorithm


    
