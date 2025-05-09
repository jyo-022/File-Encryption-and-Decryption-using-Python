from cryptography.fernet import Fernet
key=Fernet.generate_key()
with open('mykey.key','wb') as mykey:
    mykey.write(key)
with open ('mykey.key','rb') as mykey:
    key=mykey.read()
print(key)  

f=Fernet(key)
with open('encrypt_decrypt.txt','rb') as original_file:
    original=original_file.read()
encrypted=f.encrypt(original)
with open('enc_encrypt_decrypt.txt','wb') as encrypted_file:
    encrypted_file.write(encrypted)

f=Fernet(key)
with open('enc_encrypt_decrypt.txt','rb') as encrypted_file:
    encrypted=encrypted_file.read()
decrypted=f.decrypt(encrypted)

with open('dec_encrypt_decrypt.txt','wb') as decrtpted_file:
    decrtpted_file.write(decrypted)