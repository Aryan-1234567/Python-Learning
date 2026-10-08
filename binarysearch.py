#how does a binary search work?
#1. checks value in centre of array
#2. if lower, next value is check in corner of left half
#3. halves search area until value found

#the code for binary search

def binarySearch(array, Value):
    left = 0    #lower limit
    right = len(array) - 1      #upper limit

    while left <= right:
        mid = (left + right) // 2    #midpoint of the array

        if array[mid] == Value:
            return mid

        elif array[mid] < Value:
            left = mid + 1  #searches right value: middle value too small

        else:
            right = mid - 1 #Searches left half: middle value too big
    return -1  #this displays if the value isnt found

items = [1,4,6,8,10,15,27,49]
x = 4
result = binarySearch(items, x)

if result != -1:
    print(f'found at the index {result}')
else:
    print(f'not found')


