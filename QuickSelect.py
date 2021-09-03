def quickSelect(arr,left,right,k):
    #if we reach a base case where the subarray has one value
    #we have found our kth lowest value
    if  left == right:
        return arr[left] 
        # if the list contains only one element return that element

    pIndex = right
    #The pivot is the last position in our array
    
    pIndex = partition(arr, left, right)

    if k == pIndex:
        return arr[k]
        # base case
    elif k < pIndex:
        # if k is less than the pivot 
        return quickSelect(arr, left, pIndex -1, k)
    else:
        # if k is more than the pivot
        return quickSelect(arr, pIndex + 1, right, k)

    
def partition(arr, l, r):
        pivot = arr[r]
        #set our pivot to the last number in our array
        i = l -1
        # our i variable will start at the position one left of our left array on the first pass        [10,20,30,40,50]
                                                                                                       ^ ^
                                                                                                      'i j'
        #set our i variable to one less than our l array
        for j in range(l, r):
            # move j from the left of the entire array until the end of the array
            # left to right
            if arr[j] <= pivot:
                # if our current value j between left side of array to ride side array
                #is greater than our current pivot
                i += 1
                # increase i plus one to the right
                arr[i], arr[j] = arr[j], arr[i]
                #swap our current i position with our current j position
        arr[i+1], arr[r] = arr[r], arr[i+1]
            #after the numbers have been partitioned swap our i+1 position with our pivot postion at the end of the array

        return i + 1
            #return our pivot in its new postion in i+ 1 after the swap


arr = [345,97,93029,20,1,4,19,22,3,6,25]
k = 6
# k is the lowest value postion were finding
#e.g. in a sorted array of [10,20,30,40,50,60]
#k = 0 would return the lowest number = 10 k=1 would return the 2nd lowest number = 20
quickly_sorted = str(quickSelect(arr, 0, len(arr)-1,k))
#len(arr)-1 returns the last value of the array
printing= f"The {k+1}th smallest value is in k[{k}] which returns the value:"
#k+1 because arrays start at 0

print(printing + quickly_sorted) 
