
import test

def __partition(arr, left, right):
    v = arr[left]
    j = left
    for i in range(left+1, right):
        if arr[i] < v:
            arr[j+1], arr[i] = arr[i], arr[j+1]
            j += 1
    arr[left], arr[j] = arr[j], arr[left]
    return j

def __quickSort(arr, left, right):
    if left >= right-1:
        return
    
    p = __partition(arr, left, right)
    __quickSort(arr, left, p)
    __quickSort(arr, p+1, right)

@test.timer
def quickSort(arr):
    __quickSort(arr, 0, len(arr))
