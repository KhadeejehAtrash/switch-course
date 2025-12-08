# Write a recursive function that will find all permutations of a list.
# Example:
# For [1,2,3] it should return: 
# [[1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]]

def permutations(lst):
    if len(lst) == 0:
        return [[]]  

    result = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for p in permutations(remaining):
            result.append([current] + p)  

    return result


print(permutations([1,2,3]))
