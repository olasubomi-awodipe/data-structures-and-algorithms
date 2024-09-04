def binary_search(my_list, target, start_index, end_index):
    # Initialize end_index if not provided
    if end_index is None:
        end_index = len(my_list) - 1

    # Base case: the list is empty
    if start_index > end_index:
        return -1

    # Get the midpoint
    midpoint = (start_index + end_index) // 2    

    # Compare midpoint to target
    if my_list[midpoint] == target:
        return midpoint

    # Search in the left half
    elif my_list[midpoint] > target:
        return binary_search(my_list, target, start_index, midpoint-1)

    # Search in the right half
    else:
        return binary_search(my_list, target, midpoint+1, end_index)
