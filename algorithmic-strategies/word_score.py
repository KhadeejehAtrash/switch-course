# Given a string of words, you need to find the highest scoring word. Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
# ○	You need to return the highest scoring word as a string.
# ○	If two words score the same, return the word that appears earliest in the original string.
# ○	All letters will be lowercase and all inputs will be valid.


import string
SCORE = {ch: i+1 for i, ch in enumerate(string.ascii_lowercase)}

def word_score(word):
    total = 0
    for ch in word:
        total += SCORE.get(ch, 0)  
    return total

def highest_scoring_word(sentence):
    words = sentence.split(" ")  
    best_word = ""
    max_score = 0

    for word in words:
        score = word_score(word)
        if score > max_score:
            max_score = score
            best_word = word
    return best_word  

best = highest_scoring_word("b c apple")
print(f"Highest scoring word: {best}")


