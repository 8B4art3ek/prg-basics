###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

i = 0

while i < len(text):
    char = text[i]
    if char in vowels:
        vowel_count += 1 
    i += 1
    
print(f"The number of vowels in the text is: {vowel_count}")
