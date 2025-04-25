def encrypt_char(c, n, m):
    if 'a' <= c <= 'z':
        if 'a' <= c <= 'm':
            shift = n * m
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            shift = n + m
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        if 'A' <= c <= 'M':
            shift = n
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            shift = m ** 2
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c


def decrypt_char(c, n, m, original_c):
    if 'a' <= original_c <= 'z':
        if 'a' <= original_c <= 'm':
            shift = n * m
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        else:
            shift = n + m
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= original_c <= 'Z':
        if 'A' <= original_c <= 'M':
            shift = n
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            shift = m ** 2
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
    else:
        return c


def encrypt_text(text, n, m):
    return ''.join(encrypt_char(c, n, m) for c in text)


def decrypt_text(encrypted_text, original_text, n, m):
    return ''.join(decrypt_char(c, n, m, orig) for c, orig in zip(encrypted_text, original_text))


def check_correctness(original_text, decrypted_text):
    return original_text == decrypted_text


def main():
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    with open("raw_text.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()

    encrypted = encrypt_text(raw_text, n, m)
    with open("encrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(encrypted)
        print("Excrypted text: ",encrypted)
        print("\n\n<---------------------------------------------->")
        print("Encryption complete. Encrypted text saved to 'encrypted_text.txt'.")
        print("<---------------------------------------------->")

    # Use original raw_text to guide the decryption
    decrypted = decrypt_text(encrypted, raw_text, n, m)

    if check_correctness(raw_text, decrypted):
        print("\n\nDecrypted Text: ",decrypted)
        print("Decryption verified successfully!")
    else:
        print("Decryption failed. The texts do not match.")


if __name__ == "__main__":
    main()
