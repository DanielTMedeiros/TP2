def quicksort(arr):
    def partition(low, high):
        pivot = arr[high] 
        i = low - 1  
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i] 
        arr[i + 1], arr[high] = arr[high], arr[i + 1] 
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr

array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(quicksort(array))
