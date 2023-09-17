def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure shift is within the alphabet range
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            elif char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            shifted_char = char
        encrypted_text += shifted_char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            plaintext = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(plaintext, shift)
            print("Encrypted text:", encrypted_text)
        elif choice == "2":
            ciphertext = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(ciphertext, shift)
            print("Decrypted text:", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
