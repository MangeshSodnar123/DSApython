#you are given a knapsack with capacity. You need to choose from fruits to fill the sack but make a maximum profit. You can't take a fraction of the fruits.

#make a fruit class that has weight and profit as aproperties
class Fruit:
    def __init__(self,weight,profit):
        self.weight = weight
        self.profit = profit
        
#make some fruits and store them in item list
#func(items:list,capacity:int,currInd:int): ->maxProfit:int
def knapsack(items,capacity,currInd):
    #base condition.
    if capacity <= 0 or currInd>=len(items):
        return 0
    #recursive condition.
    elif(items[currInd].weight<capacity):
        profit1 = items[currInd].profit + knapsack(items,capacity-items[currInd].weight,currInd+1)
        profit2 = knapsack(items,capacity,currInd+1)
        return max(profit1,profit2)
    else:
        return 0
        
        
mango = Fruit(3,31)
apple = Fruit(1,26)
orange = Fruit(2,17)
banana = Fruit(5,72)

items = [mango,apple,orange,banana]
capacity = 7
print(knapsack(items,capacity,0))
