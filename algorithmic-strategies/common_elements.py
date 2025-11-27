# Common elements 
# Find the common elements between 2 arrays.
# 1.	Write the brute force solution
# 2.	Write a solution in O(n)

# brute force 

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]

common_elements = []

for x in arr1:
    if x in arr2:   
        common_elements.append(x)

print(common_elements)
