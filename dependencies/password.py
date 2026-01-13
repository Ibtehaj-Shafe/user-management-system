# from pwdlib import PasswordHash

# password_hashed = PasswordHash.recommended()
# def hash_password(password):
#     return password_hashed.hash(password)

# def verify_password(plain_password,hashed_password):
#     return password_hashed.verify(plain_password, hashed_password)

import bcrypt

def hash_password(password):
    pswd=password
    bytecode=pswd.encode('utf-8')
    salt=bcrypt.gensalt()
    hashed_pswd= bcrypt.hashpw(bytecode,salt)
    return hashed_pswd.decode('utf-8')

def verify_password(plain_password,hashed_password):
    # converted=hash_password(plain_password)
    # if converted == hashed_password:
    #     return True
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

