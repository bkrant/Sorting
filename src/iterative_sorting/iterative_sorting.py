# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        smallest = min(arr[i+1:])
        smallest_index = arr.index(smallest)
        if smallest < arr[i]:
            arr_i = arr[i]
            arr[i] = smallest
            arr[smallest_index] = arr_i
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:
        swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp_i = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp_i
                swaps += 1
        if swaps == 0:
            break
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr