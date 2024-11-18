
def diagonalDifference(arr):
    s1=0
    s2=0
    n=len(arr)
    for i in range(n):
        s1+=arr[i][i]
        s2+=arr[i][n-i-1]
    return abs(s1-s2)
