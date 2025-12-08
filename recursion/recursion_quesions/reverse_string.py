### **Reverse a String**

# Write a recursive function that returns the reversed version of a string.

def reverse_string(text):
    if text == "":         
        return ""
    return reverse_string(text[1:]) + text[0] 

print(reverse_string("car"))  
print(reverse_string("hello")) 
