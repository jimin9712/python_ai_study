# 함수: 아핀 암호화
def affine_encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(((key[0] * (ord(char) - 65) + key[1]) % 26) + 65)
        elif char.islower():
            result += chr(((key[0] * (ord(char) - 97) + key[1]) % 26) + 97)
        else:
            result += char
    return result

# 함수: 아핀 복호화
def affine_decrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(((modinv(key[0], 26) * (ord(char) - 65 - key[1])) % 26) + 65)
        elif char.islower():
            result += chr(((modinv(key[0], 26) * (ord(char) - 97 - key[1])) % 26) + 97)
        else:
            result += char
    return result

# 함수: 모듈러 역수 계산
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# 원문
text = "Opportunities don’t happen. You create them."
key = (3, 2)

# 암호화
encrypted_text = affine_encrypt(text, key)
print("암호화된 문장:", encrypted_text)

# 복호화
decrypted_text = affine_decrypt(encrypted_text, key)
print("복호화된 문장:", decrypted_text)

# 복호키 구하기
mod_inverse = modinv(key[0], 26)
decryption_key = (mod_inverse, -key[1] * mod_inverse % 26)
print("복호키:", decryption_key)