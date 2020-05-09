# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    n = len(q)
    
    i = n-1
    while i >= 0:        
        diff = q[i] - (i+1)
        if ( diff > 2):
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if(q[j] > q[i]):
                count = count + 1
        i = i - 1
    print(count)

minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])
#minimumBribes([2, 1, 5, 3, 4])
#minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
