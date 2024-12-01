"""
Q.1 Given an array of integers nums and an integer target, return the indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the 
same element twice.
You can return the answer in any orde
"""


def return_index(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []    

if __name__ == "__main__":
    nums = [5, 6, 7, 8]
    target = 15
    res=return_index(nums, target)
    print(res)


"""
the main logic behind the above solution is we use enumerate function that will allow us to find the index and vlaue at a same time
calculation logic is, Each number's compliment is checked against the number inside of the dictionary which avoids nested loops because we store previously encountered numbers in that very dictionary and perform a lookup, which is much faster.


The time complexity of the above solution is already o(1) which is less than the o(n^2) below is the written algorith with the calculation of time complexityy
1. Initialize the empty dictionary that will later store integer value as key and its index as value.
    > time Complexity is o(1)
2. we use loop in for each ietms in a list of integers ,to avoid time complexity o(n^2) we use enumerate which is a built in python functions that deals with index and its value at a time o(n)
    >time Complexity is o(n) for iterating items in the list
3. we complemment the current integer with tageted value, and check if the complement value exist in the dictionary it return the required indexes of the integers, O(1)
    >time complexity is o(1)
4. if the complemnt does not exist in the dictionary..it continues the execution 
    >time complexity is o(1)
5. if the inters sums does not equals the tagets it return the empty list
    >time complexity is o(1)

Overall the time complexity is o(n) because the operation is execution stops with single traversal of list   
    
"""