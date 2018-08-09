
import test

def __merge(arr, left, mid, right):
    aux = []
    for idx in range(left, right):
        aux.append(arr[idx])

    i = left; j = mid
    for k in range(left, right):
        if i >= mid:
            arr[k] = aux[j-left]
            j += 1
        elif j >= right:
            arr[k] = aux[i-left]
            i += 1
        elif aux[i-left] < aux[j-left]:
            arr[k] = aux[i-left]
            i += 1
        else:
            arr[k] = aux[j-left]
            j += 1
 
def __mergeSort(arr, left, right):
    if left >= right-1:
        return

    mid = (left+right) / 2
    __mergeSort(arr, left, mid)
    __mergeSort(arr, mid, right)
    __merge(arr, left, mid, right)

@test.timer
def mergeSort(arr):
    __mergeSort(arr, 0, len(arr))
