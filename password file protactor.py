import hashlib
import os

password = "pass00"
hash_object = hashlib.sha256(password.encode())
hex_pass = hash_object.hexdigest()

# # Write the hash to a file
# with open("password_hash.txt", "w") as f:
#     f.write(hex_dig)

# # Read the hash from the file
# with open("password_hash.txt", "r") as f:
#     stored_hash = f.read()

# Compare the stored hash with a user input password
input_password = input("Enter your password: ")
input_hash_object = hashlib.sha256(input_password.encode())
input_hex_dig = input_hash_object.hexdigest()

if hex_pass == input_hex_dig:
    print("Password is correct!")
    os.system("python PassGen.py")    
else:
    print("Password is incorrect.")
