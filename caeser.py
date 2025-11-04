def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Example usage
message = "Hello World!"
shift = 4

encrypted = caesar_cipher(message, shift, 'encrypt')
decrypted = caesar_cipher(encrypted, shift, 'decrypt')

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
