def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: The sorted array.
    """
    a = len(array)
    b = a // 2
    left_array = []
    right_array = []
    complete_array = []
    k = l = 0

    if a == 1:
        return array
    else:
        for i in range(0, b):
            left_array.append(array[i])
        for j in range(b, a):
            right_array.append(array[j])

    print(left_array)
    left_array = merge_sort(left_array)

    print(right_array)
    right_array = merge_sort(right_array)

    while k < len(left_array) and l < len(right_array):
        if left_array[k] <= right_array[l]:
            complete_array.append(left_array[k])
            k += 1
        else:
            complete_array.append(right_array[l])
            l += 1

    complete_array += left_array[k:]
    complete_array += right_array[l:]

    return complete_array


def fib(n):
    """
    Calculate the Fibonacci's series value for integer n

    Parameters:
    - n: The number to use in the Fibonacci's series.

    Returns: The calculated value of the Fibonacci's series for n
    """
    d = 0
    x = 0
    y = 1

    if n == 0 or n == 1:
        return 1

    for i in range(n-1):
        new = x + y
        x = y
        y = new
        d = x + y

    return d


def min_coins(face_values, amount):
    result = []
    for face_value in sorted(face_values, reverse=True):
        calculated = amount // face_value
        amount -= calculated * face_value
        result.append(calculated)
    return result

min_coins([25, 10, 5, 1], 41)

