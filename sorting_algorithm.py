import sys
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#Quick Sort
def partition(arr, low, high):
    # Choose the pivot. In this case, the last element.
    pivot = arr[high]

    i = low - 1

    # Traverse through the array and move all smaller elements
    # on the left side, and larger elements on the right side
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Move pivot to the position after the last smaller elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # return pivot index
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)

        # Recursion calls for both left and right part of pivot
        quick_sort(arr, low, pivotIndex - 1)
        quick_sort(arr, pivotIndex + 1, high)

# Radix Sort
def countingSortByDigit(arr, digitPos, radix = 10):
    length = len(arr)

    # The output array that will have sorted elements
    output = [0] * length
    count = [0] * radix

    # Count the occurences of each digit, store them in count[]
    for element in arr:
        index = (element // digitPos) % 10
        count[index] += 1

    # Counted values Accumulation
    for i in range(1,radix):
        count[i] += count[i-1]

    # Build the output array
    i = length-1
    while i>=0:
        index = (arr[i] // digitPos) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
        
    # Copying the output to arr, return arr
    for i in range(0,len(arr)):
        arr[i] = output[i]

# Implement radix_sort by doing countingSortByDigit for every digits
def radix_sort(arr):
    maxValue = max(arr)
    digitPos = 1
    while maxValue // digitPos > 0:
        countingSortByDigit(arr, digitPos)
        digitPos *= 10

# Linear Search
def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
        
    return indices