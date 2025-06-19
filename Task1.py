def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift) 
def main():
    print("=== Caesar Cipher ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter the message: ")
    
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift. Please enter an integer.")
        return
    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("Decrypted Message:", decrypted)
    else:
        print("Invalid choice. Please type 'e' or 'd'.")
if __name__ == "__main__":
    main()
