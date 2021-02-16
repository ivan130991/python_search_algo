def binary_search(x, arr):
    left_idx = 0
    right_idx = len(arr)-1
    while left_idx <= right_idx:
        mid = left_idx + (right_idx - left_idx) // 2
        mid_value = arr[mid]
        if x == mid_value:
            break
        elif x > mid_value:
            left_idx = mid + 1
        elif x < mid_value:
            right_idx = mid - 1
    if left_idx > right_idx:
        print("There is no number {} in array.".format(x))
    else:
        print("The index of number {} in array is at {}.".format(x, mid))


test_array = [65, 49, 84, 72, 20, 5, 92, 18, 71, 56, 61, 3]

binary_search(71, test_array)