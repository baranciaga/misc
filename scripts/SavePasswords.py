import base64
import bcrypt
import hashlib


def generate_hash(password: str):
    password = password.encode("utf-8")
    password = base64.b64decode(hashlib.sha256(password).digest())
    print(password)
    hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt(12))

    return hashed_pw.decode()


def check_password(password: str, hash: str):
    password = password.encode("utf-8")
    password = base64.b64decode(hashlib.sha256(password).digest())
    hash = hash.encode("utf-8")
    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False

password = "1234567890"*8
hash = generate_hash(password)

password2 = "01234340"*8
hash2 = generate_hash(password2)
print(hash)
print(check_password(password, hash))
print(check_password(password, hash2))
