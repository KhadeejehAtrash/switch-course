# Fibonacci Sequence
# -	Problem: Write a recursive function that returns the nth number in the Fibonacci sequence.
# -	Example Input: fibonacci(6)
# -	Expected Output: 8


# RECURSIVE 
def get_fibonacci_value(index):
    if index <= 0:
       return 0
    if index == 1:
        return 1 
    return get_fibonacci_value(index -1) + get_fibonacci_value(index-2)


print(get_fibonacci_value(0))
print(get_fibonacci_value(1))
print(get_fibonacci_value(5))
print(get_fibonacci_value(6))
print(get_fibonacci_value(8))