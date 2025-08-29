def has_double_vowel(word):
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i+1] in vowels:
            return True
    return False

def words_with_double_vowel(words):
    return [word for word in words if has_double_vowel(word)]

# Example usage:
word_list = ["book", "tree", "queue", "moon", "apple", "rain"]
result = words_with_double_vowel(word_list)
print(result)  # Output: ['tree', 'queue', 'moon']