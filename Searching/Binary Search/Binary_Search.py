def search(arr, key):
    first = 0
    last = len(arr) - 1

    while(first <= last):
        mid = (first + last) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            last = mid - 1
        else:
            first = mid + 1
    return "Element not found"

arr = [1, 2, 4, 3, 6, 9]
key = 10
ind = search(arr, key)
print(ind)

