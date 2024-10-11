def quickselect(arr, k):
    def partition(low, high):
        pivot = arr[high]  
        i = low - 1  
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i] 
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  
        return i + 1

    def quickselect_recursive(low, high, k):
        if low == high:  
            return arr[low]

        pivot_index = partition(low, high)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect_recursive(low, pivot_index - 1, k)
        else:
            return quickselect_recursive(pivot_index + 1, high, k)
    return quickselect_recursive(0, len(arr) - 1, k - 1)

array = [10, 9, 8, 7, 6, 5]
print(quickselect(array, 4))