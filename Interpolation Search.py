def interpolationSearch(num, arr):
    low = 0
    high = len(arr)-1
    pos = int(low + ((int(high - low) / (int(arr[high]) - int(arr[low])))) * (num - int(arr[low])))
    while arr[pos] != num:
        if high < low or high < 0 or low < 0:
            pos = -1
            break
        else:
            pos = int(low + ((int(high - low) / (int(arr[high]) - int(arr[low])))) * (num - int(arr[low])))
        if num > arr[pos]:
            low = pos
            high = high - pos -1
        else:
            high = pos
    if pos == -1:
        return "There is no element {} in array".format(num)
    else:
        return "Element {} is at index {} of array".format(num, pos)

test_arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]  
print (interpolationSearch(19, test_arr))