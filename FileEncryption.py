from cryptography import encrypt, decrypt

user_input = input("Enter a String : ")

encryption = encrypt(user_input)
decryption = decrypt(user_input)

print(f'The Encrypted Message Is : {encryption}')
print(f'The Decrypted Message Is : {Decryption}')