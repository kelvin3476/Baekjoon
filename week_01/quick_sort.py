def quick_sort(arr):
    def recursive(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        recursive(low, mid - 1)
        recursive(mid +1, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        i = low
        j = high
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1 
                j -= 1
        return i

    return recursive(0, len(arr) - 1)

arr = [3,2,1,4,7,6,5]
quick_sort(arr)
print(arr)
 