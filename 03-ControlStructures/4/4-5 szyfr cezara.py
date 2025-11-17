###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
shift = 1       # liczba przesunięć

for char in plain_text:
    if char.islower():
        # (ord(char) - ord('a')) -> 'a' staje się 0, 'b' staje się 1...
        # (% 26) -> 'z' (25) + 1 = 26. 26 % 26 = 0 (czyli 'a')
        # + ord('a') -> przesuń z powrotem do ASCII
        new_char_code = ((ord(char) - ord('a') + shift) % 26) + ord('a')
        encrypted_text += chr(new_char_code)
    elif char.isupper():
        new_char_code = ((ord(char) - ord('A') + shift) % 26) + ord('A')
        encrypted_text += chr(new_char_code)
    else:
        encrypted_text += char   # Zostaw spacje/symbole w spokoju

print(f"Plain text: {plain_text}")
print(f"Encrypted text: {encrypted_text}")