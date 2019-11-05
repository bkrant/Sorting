# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    ma = []

    if arrA == []:
      return arrB
    
    elif arrB == []:
      return arrA
    
    elif arrA[0] > arrB[0]:
      ma = ma + [arrB[0]] + merge(arrA, arrB[1:])
    
    else:
      ma = ma + [arrA[0]] + merge(arrA[1:], arrB)

    return ma


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

  if len(arr) <= 1:
    return arr

  else:
    first = arr[:len(arr)//2]
    second = arr[len(arr)//2:]

    return merge(merge_sort(first), merge_sort(second))

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
