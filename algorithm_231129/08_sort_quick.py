arr = [10, 12, 17, 25, 55, 22, 35, 73, 99, 48, 5, 7]

def quick_sort(arr, start, end):
    if start >= end:
        return arr
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[start]:
            left += 1
        while right > start and arr[right] >= arr[start]:
            right -= 1
        if left > right:
            arr[start], arr[right] = arr[right], arr[start]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)