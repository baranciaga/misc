import time
import pyotp

def gen_key():
    return pyotp.random_base32()


def gen_url():
    return pyotp.totp.TOTP(key).provisioning_uri(name='Baran', issuer_name='2FA-APP')


def generate_code(key: str):
    totp = pyotp.TOTP(key)
    return totp.now()


def verify_code(key : str, code: str):
    totp = pyotp.TOTP(key)
    return totp.verify(code)

key = gen_key()
print(key)
uri = gen_url()
print(uri)

code = generate_code(key)
print(code)
time.sleep(5)
code2 = generate_code(key)

### false ex
key2 = gen_key()
code3 = generate_code(key2)

print(verify_code(key, code))
print(verify_code(key, code2))