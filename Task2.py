from PIL import Image
import os

def encrypt_image(image_path, key, output_path):
    """
    Encrypts the image using XOR operation on each pixel value.

    Parameters:
    - image_path (str): Path to the input image.
    - key (int): Integer key for encryption.
    - output_path (str): Where to save the encrypted image.
    """
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure RGB mode

    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR each color channel with the key
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(encrypted_path, key, output_path):
    """
    Decrypts the image using XOR operation with the same key.

    Parameters:
    - encrypted_path (str): Path to the encrypted image.
    - key (int): Same key used during encryption.
    - output_path (str): Where to save the decrypted image.
    """
    encrypt_image(encrypted_path, key, output_path)
    print(f"Decrypted image saved to {output_path}")


def main():
    print("=== Simple Image Encryption Tool ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    image_path = input("Enter image file path: ")
    key = int(input("Enter numeric key (0-255): "))

    if not os.path.exists(image_path):
        print("File not found!")
        return

    if choice == 'e':
        output = "encrypted_image.png"
        encrypt_image(image_path, key, output)
    elif choice == 'd':
        output = "decrypted_image.png"
        decrypt_image(image_path, key, output)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
