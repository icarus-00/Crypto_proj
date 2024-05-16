from sympy import mod_inverse

alphabet = "abcdefghijklmnopqrstuvwxyz"

def affine_encryption(plaintext, a, b):
    ciphertext = ''
    for p_ch in plaintext:
        if p_ch.isalpha():
            p_value = alphabet.index(p_ch)
            c_value = (a * p_value + b) % 26
            c_ch = alphabet[c_value]
            ciphertext += c_ch
        else:
            continue
    return ciphertext

def affine_decryption(ciphertext, a, b):
    plaintext = ''
    inv = mod_inverse(a, 26)
    for c_ch in ciphertext:
        c_value = alphabet.index(c_ch)
        p_value = (inv * (c_value - b)) % 26
        p_ch = alphabet[p_value]
        plaintext += p_ch
    return plaintext




print(affine_decryption("hlzhpf",3,2))