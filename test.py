
import random
import time

def random_arr(len, start, end):
    assert(len > 0)
    assert(end > start)
    arr = []
    for i in range(len):
        arr.append(random.randint(start, end))
    return arr

def nearlyOrder_arr(len, swap):
    arr = []
    for i in range(len):
        arr.append(i)

    for idx in range(swap):
        posx = random.randint(0, len-1)
        posy = random.randint(0, len-1)
        arr[posx], arr[posy] = arr[posy], arr[posx] 
    return arr

def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def timer(func):
    def wrapper(arr):
        t0 = time.time()
        func(arr)
        t1 = time.time()
        status = isSorted(arr)
        print ("Total time running %s: %s seconds, status: %s" %
               (func.func_name, str(t1-t0), status))
    return wrapper


