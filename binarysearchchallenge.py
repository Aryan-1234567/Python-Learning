def binarySearch(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == value:
            return mid

        elif array[mid] < value:
            left = mid + 1 #searches right side

        else:
            right = mid -1 #searches left side

    return -1 #if value not found

items = [3, 7, 12, 18, 24, 31, 39, 46, 52, 61, 68, 75, 83, 91, 97] 
x = 75
result = binarySearch(items, x)

if result != -1:
    print(f'item found at index {result}')
else:
    print(f'not found')





#example 2:
def binarysearch(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1 #searches right
        else:
            right = mid - 1 #searches left
    return -1 #if value not found

items = [4, 9, 15, 22, 28, 35, 41, 47, 53, 60, 67, 74, 81, 89, 96, 103, 110]
x = 81
result = binarysearch(items, x)
if result != -1:
    print(f'item found at {result}')
else:
    print(f"item not found in the array")
