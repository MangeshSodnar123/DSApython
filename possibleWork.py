#Activity selection problem

#declare a activity dictionary containing activity as a key, and start and end timing as a value (list)

#declare a activity interval dictionary and store the interval of each activity using for loop

#store all these intervals in a list
#sort that list in ascending order

#declare a function that takes a time as a input and gives all possible activity list as a output
    #loop through the sorted list and add the interval in the variavle called possibleWork
        #run a loop till possibleWork is less than equal to time(input of a function)
        #at the same time keep storing those intervals in a possibleIntervals list
    
    #now run a loop for possibleIntervals list:
        #find a key of interval dictionary using each element of the possibleIntervals list
        #store those keys in new lsit 
