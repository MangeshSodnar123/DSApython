#Activity selection problem

#declare a activity dictionary containing activity as a key, and start and end timing as a value (list)
activity = {
    'a1':[1,4],
    'a2':[1,5],
    'a3':[1,7],
    'a4':[1,8],
    'a5':[1,5],
    'a6':[1,9],
    'a7':[1,4],
    'a8':[1,2],
    'a9':[1,3],
    'a10':[1,6]
}
#declare a activity interval dictionary and store the interval of each activity using for loop
interval = {}
intervalList = [] # for sorting the differences,

for key,value in activity.items():
    span = value[1]-value[0]
    interval[key] = span
    intervalList.append(span)
    
# print(activity)
# print('--------------------')
# print(interval)
#store all these intervals in a list
#sort that list in ascending order
intervalList.sort()
# print(intervalList)
#declare a function that takes a time as a input and gives allpossible activity list as a output
def possibleActivities(time):
    possibleWork = 0
    index = 0
    #loop through the sorted list and add the interval in the variavle called possibleWork
    while (possibleWork<=time)
        #run a loop till possibleWork is less than equal to time(input of a function)
        #at the same time keep storing those intervals in a possibleIntervals list
        possibleWork += intervalList[index]
        index += 1
        possibleIntervals
    
    #now run a loop for possibleIntervals list:
        #find a key of interval dictionary using each element of the possibleIntervals list
        #store those keys in new list or just print them one by one with some message
