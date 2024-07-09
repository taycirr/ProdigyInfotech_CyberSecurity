def caesar_cipher(text, shift):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Normalize the shift to ensure it's within the range of 0-25
    shift = shift % 26
    
    # Create a shifted version of the alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # Create a translation table
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    # Translate the text using the translation table
    return text.translate(table)

# Get user input for the text and shift value
plain_text = input("Enter the text you want to encrypt/decrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message
cipher_text = caesar_cipher(plain_text, shift)
print(f"Encrypted: {cipher_text}")

# Decrypt the message
decrypted_text = caesar_cipher(cipher_text, -shift)
print(f"Decrypted: {decrypted_text}")
