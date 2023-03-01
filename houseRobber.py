#house robber problem
#declare a function(houseList,index)
    #if index>=len(houseList)
        #return 0
    #else
        #robfirstHouse = houseList[index] + function(houses,index+2)
        #skipFirstHouse = function(houses,index+1)
        #return max(robfirstHouse,skipFirstHouse)
        
def houseRobber(houses,index):
    if index>=len(houses):
        return 0
    else:
        robFirstHouse = houses[index] + houseRobber(houses,index+2)
        skipFirstHouse = houseRobber(houses,index+1)
        return max(robFirstHouse,skipFirstHouse)
        
houses = [6,7,1,30,8,2,4]
print(houseRobber(houses,6))
