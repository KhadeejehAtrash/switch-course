### 3️⃣ **Factorial**

# Write a recursive function that computes `n!`.


def get_factorial(number):
    if number == 0 :
        return 1
 
    result = number * get_factorial(number - 1)
    return result

print(get_factorial(9))
    