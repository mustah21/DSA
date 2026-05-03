def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    j = len(array)
    for i in range(1,j):
        key = array[i]
        for k in range(i, 0, -1):
            if key < array[k - 1]:
                array[k], array[k - 1] = array[k - 1], array[k]

array2 = [6, 8, 5, 1, 2]
insertion_sort(array2)
print(array2)



def quick_sort(array, left_index=None, right_index=None):
    # Set these values so the function can be called by the user with only the array as parameter

    if not left_index:
        left_index = 0
    if not right_index:
        right_index = len(array) - 1
        # The pivot selection is a problem in its own.
        # For now let's use the first element, but any other element could have been chosen
        # (with necessary algorithm's adjustments)

    pivot_index = left_index

    # We set a border index to indicate that values less or equal than pivot are to
    # its left (border index inclusive) and values bigger than pivot are at its right,
    # right now the only element less or equal than the pivot, is the pivot itself.
    border_index = left_index
    # And start traversing the partition

    for current in range(left_index+1, right_index+1):
        # if the value of the current position is less than pivot,
        # let's add it (current value) to the minors part

        if array[current] <= array[pivot_index]:
            # Update border as there is one minor more now.
            border_index += 1

        # Check if we actually need to do the swap. If current index was
        # the next value after minors, then no swap is necessary
        if current > border_index:
            # If that was not the case, then swap their values
            array[current], array[border_index] = array[border_index], array[current]
        # After traversing the partition, the pivot can be swapped with the last of the minors.
        # If pivot is the only minor, then there is no need to swap.


    if border_index != pivot_index:
    # swap
        array[border_index], array[pivot_index] = array[pivot_index], array[border_index]
        pivot_index = border_index # Update pivot index after swap
    # The pivot is in its position and all values less or equal than pivot are at the left,
    # and all values bigger than pivot are at the right.
    # Now call recursively this function on both partitions.
    # Check if left partition has at least 2 elements

    if (pivot_index - left_index) > 1:
       quick_sort(array, left_index, pivot_index-1)
        # Check if right partition has at least 2 elements
    if (right_index - pivot_index) > 1:
        quick_sort(array, pivot_index+1, right_index)