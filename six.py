def findWater(arr):

    n = len(arr)
    left = [0] * n
    right = [0] * n
    res = 0

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    for i in range(1, n - 1):
        minOf2 = min(left[i - 1], right[i + 1])
        if minOf2 > arr[i]:
            res += minOf2 - arr[i]

    return res

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(findWater(arr))