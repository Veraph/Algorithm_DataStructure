# quick_sort.py -- use D&C thinking to sort an arrary
# average complexity: O(nlogn) / worst: O(n^2)
# because of const, quick_sort is faster than merge sort on average

def quicksort(arr):
    '''quick sort algorithm'''
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

result = quicksort([3, 1, 20, 99, 2, 1, 5])
print(result)