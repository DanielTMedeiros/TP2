import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = random.sample(range(1, 10001), 10000)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time



print(f"BubbleSort time: {measure_time(bubblesort, arr)} seconds")
print(f"QuickSort time: {measure_time(quicksort, arr)} seconds")