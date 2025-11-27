# Largest of 3
# Write a function that receives 3 numbers and return the biggest one.
# You are not allowed to use any functions including built in ones.


def largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(largest_of_three(5, 9, 3))  
print(largest_of_three(12, 7, 12)) 
print(largest_of_three(1, 2, 3))   
