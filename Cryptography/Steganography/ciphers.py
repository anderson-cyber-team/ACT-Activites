def encrypt_caesar(plain_text, shift):
    cipher_text = []
    for i in range(len(plain_text)):
        if i == len(plain_text) - 1:
            cipher_text.append(plain_text[i])
        else:
            cipher_text.append(chr((ord(plain_text[i]) + shift)))
    return "".join(cipher_text)


def decrypt_caesar(cipher_text, shift):
    plain_Text = []
    for i in range(len(cipher_text)):
        if i == len(cipher_text) - 1:
            plain_Text.append(cipher_text[i])
        else:
            plain_Text.append(chr((ord(cipher_text[i]) - shift)))
    return "".join(plain_Text)


def encrypt_vigenere(plain_text, key):
    cipher_text = []
    key = key.lower().ljust(len(plain_text))

    for pt_char, k_char in zip(plain_text, key):
        shift = ord(k_char) - ord("a")
        if pt_char.isalpha():
            ascii_offset = ord("a") if pt_char.islower() else ord("A")
            cipher_text.append(
                chr((ord(pt_char) - ascii_offset + shift) % 26 + ascii_offset)
            )
        else:
            cipher_text.append(pt_char)

    return "".join(cipher_text)


def decrypt_vigenere(cipher_text, key):
    plain_text = []
    key = key.lower().ljust(len(cipher_text))

    for ct_char, k_char in zip(cipher_text, key):
        shift = ord(k_char) - ord("a")
        if ct_char.isalpha():
            ascii_offset = ord("a") if ct_char.islower() else ord("A")
            plain_text.append(
                chr((ord(ct_char) - ascii_offset - shift) % 26 + ascii_offset)
            )
        else:
            plain_text.append(ct_char)

    return "".join(plain_text)
