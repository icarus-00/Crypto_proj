def get_modular_invers(a, b):
    x= 0
    y =1
    u = 1
    v = 0
    while a!=0:
        q = b//a
        r = b%a
        m = x-u*q
        n = y-v*q
        b = a
        a = r
        x = u
        y = v
        u = m
        v = n
    """ if b == 1:
        return x
    else:
        return None """
    gcd = b
    return gcd , x , y

def modInverse(a, m):
    g, x, y = get_modular_invers(a, m)
    if g != 1:
        return "Error ! modular inverse does not exist"
    else:
        return x%m

def affine_encrypt(plaintext, key):
    return "" . join([chr(((key[0] * (ord(t) - ord("A")) + key[1]) %26) + ord("A")) for t in plaintext.upper().replace(" ", "")])

def affine_decrypt(ciphertext, key):
    '''return "" . join([chr(((modInverse(key[0], 26) * (ord(c) - ord("A")) - key[1])) % 26) + ord("A")) for c in c"iphertext.upper().replace(" ", "")])'''
    return "".join([chr( ( ( modInverse(key[0],26) * (ord(c) -ord("A") -key[1] ))  %26  ) +ord("A")  ) for c in ciphertext])

key = [3,2]
test = affine_encrypt("omar", key)
print(test)

decrypted = affine_decrypt(test, key)
print(decrypted)


