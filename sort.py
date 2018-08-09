
import test
import copy
import mergeSort
import quickSort

@test.timer
def selectionSort(arr):
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
 
@test.timer
def insertionSort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        for j in range(i, -1, -1):
            if tmp < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                break
        arr[j] = tmp
        

if __name__ == "__main__":

    arr = test.random_arr(10000, 0, 400)
    arr1 = copy.copy(arr)
    arr2 = copy.copy(arr)
    arr3 = copy.copy(arr)

    # arr = test.nearlyOrder_arr(10, 2)

    selectionSort(arr)
    insertionSort(arr1)
    mergeSort.mergeSort(arr2)
    quickSort.quickSort(arr3)
