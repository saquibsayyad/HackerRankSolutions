
def hourglassSum(arr):
    sumsArr = []
    n=len(arr)
    i=1
    j=1
    while i < n-1:
        while j < n-1:
            sums = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            sums = sums + arr[i][j]
            sums = sums + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            sumsArr.append(sums)
            print(arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1])
            print(arr[i][j])
            print(arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1])
            j = j + 1
        j=1
        i= i + 1
    return max(sumsArr)
    

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 9, 2, -4, -4, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, -1, -2, -4, 0]]

print(hourglassSum(arr))
