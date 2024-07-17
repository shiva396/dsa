"""Note : Binary search wokrs with only sorted array"""

def search(arr, key, first, last):
    mid = (first + last) // 2
    if first > last:
        return "element not found"
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return search(arr, key, first, mid - 1)
    else:
        return search(arr, key, mid + 1, last)
    
#Driver code
arr = sorted([1, 2, 4, 3, 6, 9])
key = 3
first = 0
last = len(arr) - 1
ind = search(arr, key, first, last)
print(ind)
    