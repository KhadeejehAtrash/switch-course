
# Count vowels
# How do you count the number of vowels and consonants in a given string


def count_vowels_consonants(words):
     
    vowels = {"a", "e", "i", "o", "u"}

    vowels_counter = 0
    consonants_counter = 0

    for word in words:        
        for ch in word:        
            if ch.lower() in vowels:   
                vowels_counter += 1
            elif ch.isalpha() and ch not in vowels:
                consonants_counter += 1
    print(f"vowels: {vowels_counter}, consonants: {consonants_counter} in the word {words}")

count_vowels_consonants("hello")
count_vowels_consonants("Khadeejeh")