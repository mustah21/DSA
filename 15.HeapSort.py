def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure

    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node

    Returns: None
    """
    current = start
    left_child_index = 2 * current + 1
    right_child_index = 2 * current + 2

    while left_child_index <= end:
        largest = current
        if array[largest] < array[left_child_index]:
            largest = left_child_index

        if right_child_index <= end and array[right_child_index] > array[largest]:
            largest = right_child_index

        if largest != current:
            array[current], array[largest] = array[largest], array[current]
            current = largest
            left_child_index = 2 * current + 1
            right_child_index = 2 * current + 2
        else:
            return


array = [6, 2, 5, 8, 1]
sift_down(array, 1, 4)
print(array)


def heap_sort(array):
    # Heapify the array with a Max heap

    for start in range(len(array)//2-1, -1, -1):
        sift_down(array, start, len(array)-1)


    # As using a max heap, the heap will return the max values,
    # so they should be placed at the end of the array
    end = len(array)-1 # Last position

    # Loop while heap is not empty
    while end > 0:
        # Swap root and end places
        array[0], array[end] = array[end], array[0]
        # Decrease end. Now heap is one element shorter
        end -= 1
        # Sink the value at the root to maintain the heap property
        sift_down(array, 0, end)
