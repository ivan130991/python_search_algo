###LINEAR SEARCH###

array_list = [1,2,3,4,5,6,7,5,9,10]
def linear_search(x, arr):
    for i in range(0, len(arr)):
        if arr[i] == x:
            print("Index of element %s : " % (x), i)
            return i
    print ("Element {} is not found in array".format(x))

linear_search (11, array_list)

