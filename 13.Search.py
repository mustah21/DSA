from six import reraise


def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    start = 0
    end = len(array) - 1
    midpoint = (start + end) // 2
    found = False



    while not found:
        if array[midpoint] == value:
            found = True
            return midpoint
        else:
            if array[midpoint] < value:
                start = midpoint + 1
                midpoint = (start + end) // 2
            else:
                end = midpoint - 1
                midpoint = (start + end) // 2
        if start > end:
            return None

    return None


def interpolation_search(array, value):
    """
    Performs an Interpolation search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        if array[start] == array[end]:
            midpoint = (start + end) // 2
        else:
            midpoint = start + int((end - start) * ((value - array[start]) / (array[end] - array[start])))

        if array[midpoint] == value:
            return midpoint
        else:
            if array[midpoint] < value:
                start = midpoint + 1
            else:
                end = midpoint - 1



    return None



array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
print(interpolation_search(array, 0))
print(interpolation_search(array, 98))
print(interpolation_search(array, 29))
print(interpolation_search(array, 100))
print(interpolation_search(array, -1))
print(interpolation_search(array, 44))