def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    #set our length of list to the second to last position because we dont need to check it
    sorted = False
    #set our sorted flag to false

    while not sorted:
        sorted = True
        # set our sorted flag to true on the inital pass if the for loop completes and sorted doesnt change to false
        # that means list is fully sorted
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                print("current unsorted: " +str(list))
                #check if [i] is larger than the index to the right of it which is [i+1]
                #if its larger  change the sorted flag to false
                list[i], list[i+1] = list[i+1], list[i]
                #swap postions by changing the value of [i] to the value of [i+1] meaning the index to the right 
                # and the value of [i+1] to [i]
                print("Numbers swapped: " +str(list[i+1]) +" -> "+ str(list[i]))
                #print the numbers that have been swapped

        unsorted_until_index = unsorted_until_index - 1
        #after completing an interation reduce the range of the index by 1 because the sorted number
        #is now in the correct position


list = [65,25,45,10,25,15,1]
print("starting list: "+ str(list))
bubble_sort(list)
print("Bubble sorted list: " +str(list))

