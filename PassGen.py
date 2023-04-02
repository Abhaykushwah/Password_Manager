import random
import hashlib
import pyperclip
import sys

length = int(input('''Enter the length of your password (RECOMMENDED[9-16])
(Default[11] : ''') or "11")

possible = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890;'/.,<>?:\"/\\!@#$%^&*()_+-=`~")

def generate(length):
    global password
    password = ""
    for i in range(length):
        password+=random.choice(possible)
    print("Your Generated password is : " + password)
    return password
password =  generate(length)
# print(password)

def saveANDcopy(FOR_hash_password):
    ## Hashing Password
    hash = hashlib.md5()
    hash.update(FOR_hash_password.encode('utf-8'))
    hash_password = hash.hexdigest()
        
    ## Storing password in the from of hash
    with open("password_Hash.txt", "a") as ToSave:
        ToSave.write(hash_password+"\n")
    return hash_password 



def choice_fun(password):
    choice = int(input('''1). Copy AND Save
2). Regenerate
Enter Your Choice : '''))
    if (choice == 1 ):
        print("---------------------------------")
        print("Password Saved & copid in Clipboard")
        ## Coping password
        pyperclip.copy(password)
        # clipboard_content = pyperclip.paste()
        saveANDcopy(password) ## This Will call the fuction to save the password
        sys.exit()
    elif (choice == 2):
        print("---------------------------------")
        print("Regenrating Your password....")
        password = generate(length)
        choice_fun(password)
    else:
        print("Enter a valid choice")
        choice_fun(password)
choice_fun(password)


### Hashing 
# hash = hashlib.md5()
# hash.update(password.encode('utf-8'))
# print("Hashed password: " + hash.hexdigest())