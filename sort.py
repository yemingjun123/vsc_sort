
import test
import copy
import sys
import mergeSort
import quickSort
from maxHeap import MaxHeap

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

    # sys.setrecursionlimit(10000000)  

    # arr = test.random_arr(10000, 0, 400)
    # arr = test.nearlyOrder_arr(100000, 2)
    # arr1 = copy.copy(arr)
    # arr2 = copy.copy(arr)
    # arr3 = copy.copy(arr)

    # selectionSort(arr)
    # insertionSort(arr1)
    # mergeSort.mergeSort(arr2)
    # quickSort.quickSort(arr3)

    heap = MaxHeap()
    heap.insert(2)
    heap.insert(4)
    heap.insert(6)
    heap.insert(8)
    heap.insert(10)
    heap.insert(20)
    heap.insert(16)
    heap.insert(12)
    heap.insert(4)

    print heap.size()
    print heap.isEmpty()
    print heap.data

    print heap.dequeue()
    print heap.size()
    print heap.data