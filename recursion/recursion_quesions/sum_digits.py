# ### 1️⃣ **Sum of Digits**

# Write a recursive function that returns the sum of all digits of a number.
# Example: `sum_digits(1234) → 10`.

def sum_digits(n):
    if n == 0:       
        return 0
    else:
        last_digit = n % 10
        remaining = n // 10
        return last_digit + sum_digits(remaining)

print(sum_digits(1234))  
