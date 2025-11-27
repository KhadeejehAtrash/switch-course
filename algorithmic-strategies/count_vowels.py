
# Count vowels
# How do you count the number of vowels and consonants in a given string

words = ["hello"]   
vowels = {"a", "e", "i", "o", "u"}

vowels_counter = 0
consonants_counter = 0

for word in words:        
    for ch in word:        
        if ch.lower() in vowels:   
            vowels_counter += 1
        elif ch.lower() not in vowels:
            consonants_counter += 1

print("vowels are " + str(vowels_counter) + " consonants are " + str(consonants_counter))