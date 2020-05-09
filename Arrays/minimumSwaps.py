def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    i = 0
    while i < n:
        #print(arr[i], (i+1), arr)
        if(arr[i] != (i+1)):
            index = arr[i] - 1
            t = arr[i]
            arr[i] = arr[index]
            arr[index] = t
            swaps = swaps  + 1
        else:
            i = i + 1
    return swaps


#should return 3
#print(minimumSwaps([4, 3, 1, 2]))


#should return 3
#print(minimumSwaps([2, 3, 4, 1, 5]))

#should return 7
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))
