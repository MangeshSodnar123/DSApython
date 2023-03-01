#problem# 
#Givan an array representing n positions along a straight line. Find k elements from the array such that the minimum distance between any two points is maximized.
#tests
#[1,2,4,8,9]
#1,2,4 = 1-2 = 1,1-4 = 3, min distance = 1
#1,2,8 = 1,2 = 1
#1,2,9 = 1-2 = 1
#1,4,8 = 1-4 = 3, 1-8 = 7 =>3
#1,4,9 = 1-4 = 3,1-9 = 8 =>3

# def func(arr):
#     #sort arr ascending
#     arr.sort()
#     distArr = []
#     #loop 1
#     for i in range(len(arr)):
#         #loop 2
#         for j in range(i,len(arr)):
#             #loop 3:
#             for k in range(j,len(arr)):
#                 minDist = min(arr[k]-arr[j],arr[j]-arr[i])
#                 distArr.append(minDist)
#     distArr.sort()
#     return distArr[-1]
    
# arr = [2,4,7]
# print(func(arr))

def func(arr,start,end):
    #base condition
    arr.sort()
    mid = (start+end)//2
    if(start == end):
        return 0
    if(end-start==2):
        return min(arr[end]-arr[mid],arr[mid]-arr[start])
    else:
        return max(func(arr,start,mid),func(arr,mid+1,end))
    
arr = [1,2,4,8]
print(func(arr,0,len(arr)-1))
