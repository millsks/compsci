
def selection_sort(array: list) -> None:
    """
    A simple implementation of selection sort.

    In computer science, selection sort is an in-place comparison sorting algorithm. It has an O(n²) time complexity,
    which makes it inefficient on large lists, and generally performs worse than the similar insertion sort. Wikipedia

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n^2
    Space complexity: 1
    Method: Selection
    Stable: No
    Class: Comparison sort

    :param array:
    :return:
    """

    # Cycle through each index in the array
    for i in range(len(array)):
        # Set the minimum index to the current index in the loop
        min_idx = i

        # Cycle through the array starting from the current minimum index
        for j in range(i+1, len(array)):
            # Check if the value at the current minimum index is greater than the value
            # at the current index j of the inner loop.
            if array[min_idx] > array[j]:
                # If the value of the current minimum index is larger than the current index
                # of the inner loop, then the current minimum index becomes index j
                min_idx = j

        # Swap the value of the outer loop index i with the value of the array at the min_idx
        array[i], array[min_idx] = array[min_idx], array[i]


if __name__ == '__main__':
    import random

    # Create randomly sampled array of size ranging from 10 to 50
    array1 = random.sample(range(0,100), random.randint(10,50))

    # Print the array before we sort it
    print('Array before sort:')
    print(array1)

    # Sort the array
    selection_sort(array1)

    # Print the array after it is sorted.
    print('\nArray after sort:')
    print(array1)