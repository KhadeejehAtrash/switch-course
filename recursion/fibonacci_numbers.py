# The Fibonacci sequence is a series of numbers where each number is the sum of the two before it.

#ITERATIVE 

def fibonacci_nums(nums):
    for num in range(1, nums + 1 ):
        print(f"you take num #{num}")



# RECURSIVE 
def fibonacci_numbers(numbers):
    if numbers == 0:
       return
    fibonacci_numbers(numbers - 1)
    print(f"you take numbers #{numbers}")


fibonacci_nums(100)
fibonacci_numbers(100)