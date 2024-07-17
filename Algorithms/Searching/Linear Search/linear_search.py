def search(x, arr):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
        
arr = [1, 2, 4, 3, 6, 9]
element = 3
position = search(element, arr) + 1
print(position)