def productExceptSelf(arr):
    n = len(arr)

    if n == 1:
        return []       # if the list contains only one element , it will return empty list

    left = [1] * n
    right = [1] * n
    prod = [1] * n

    
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]  # runs n-1 times whoose time complexity will be O(n)

   
    for j in range(n - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1] #runs n-1 times whoose time complexity will be O(n)

    for i in range(n):
        prod[i] = left[i] * right[i]   #Construct the product array my multiplying the left[i] and right[i], runs n-1 times whoose time complexity will be O(n)

    return prod

if __name__ == "__main__":
    arr = [5,4, 3, 2, 1]
    res = productExceptSelf(arr)
    print(res)


"""
the above problem has timcomplexity of O(n)
becuase if we add the complexity of all these thrre loops it will be O(3n) which equals O(n).

if we had done by multiplying the all the elements and done the division by num[i],some time we may encounter 0 /integer case
"""