from cryptography.fernet import Fernet
key = Fernet.generate_key() 
# sinh khoá
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
    
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)