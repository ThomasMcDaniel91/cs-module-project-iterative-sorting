def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        # go through the values in the list one at a time
        # and check if any of them are the target value
        if arr[i] == target:
            return i
    
    # once the function has run through all the values return -1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # getting the limitations of the array
    low =  0
    high = len(arr) -1
    mid = 0
    # making sure that the lowest value is still lower than the highest after
    # the change in the upper or lower point
    while low <= high:
        # set the midpoint to check for the binary search
        mid = (high + low) // 2
        # if the target is smaller than the middle value of the array
        # we change the upper limit to the midpoint - 1 because we know
        # it isn't the middle value, lets us remove 1 more value each time
        #  we go through
        if arr[mid] > target:
            high = mid -1
        # if the target is larger than the midpoint, we move the midpoint
        # to be the low end of our search
        if arr[mid] < target:
            low = mid+1
        # if the midpoint is the target then we return the index of the value
        if arr[mid] == target:
            return mid

    # once the low end becomes larger than the high end
    # we know we have searched all values so return -1
        # not found
    return -1