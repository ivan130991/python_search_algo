import math

def jump_search(x,arr, m = 0):
    if m == 0:
        m = int(math.sqrt(len(arr)))
    element_idx = jump_search_method(x, arr, m)
    if element_idx == -2:
        print("Please enter a positive step value!")
    elif element_idx == -1:
        print("Element {} is not found in array!".format(x))
    else:
        print("Element {} is found at index {} of array!".format(x,element_idx))

def jump_search_method(x, arr, m):
    if m <= 0:
        return -2
    else:
        for i in range(0, len(arr), m):
            if x < arr[i]:
                for j in range (i-m, i+1):
                    if arr[j] == x:
                        return j
                    elif j == (i) and arr[j] != x:
                        return -1
            elif (i + m) > len(arr)-1:
                for j in range (i, len(arr)):
                    if arr[j] == x:
                        return j
                    elif j == (len(arr)-1) and arr[j] != x:
                        return -1
            else:
                continue



test_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

jump_search(144, test_array)