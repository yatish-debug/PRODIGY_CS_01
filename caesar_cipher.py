def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            cipher_char = chr((ord(char) - ascii_offset + shift * mode) % 26 + ascii_offset)
            result += cipher_char
        else:
            result += char
    return result

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Choose mode - Encrypt (E) or Decrypt (D): ")

    if mode.lower() == 'e':
        print("Encrypted text: ", caesar_cipher(text, shift, 1))
    elif mode.lower() == 'd':
        print("Decrypted text: ", caesar_cipher(text, shift, -1))
    else:
        print("Invalid mode. Please choose 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
