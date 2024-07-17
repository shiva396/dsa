def search(key, arr, curr):
    if curr == -1:
        return -1
    if arr[curr] == key:
        return curr
    return search(key, arr, curr-1)

arr = [1, 2, 4, 3, 6, 9]
key = 3
curr = len(arr) - 1

#Since, it is position so add one to the index value
position = search(key, arr, curr) 

print(position)