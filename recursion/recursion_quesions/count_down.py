### **Count Down**

# Write a recursive function that prints numbers from `n` down to `1`.

def count_down(num):
    if num == 0:          
        return
    print(f"your number #{num}")  
    count_down(num - 1)    

count_down(9)
