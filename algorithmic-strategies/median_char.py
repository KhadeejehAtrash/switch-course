# Median char 
# Find the median char (half of the letters are smaller than it, and half are bigger) in a string. Example: question => o 


def median_char(word):
    sorted_chars = sorted(word)      
    mid_index = (len(sorted_chars)-1) // 2
    median_char = sorted_chars[mid_index]
    print(median_char)              


median_char("question")