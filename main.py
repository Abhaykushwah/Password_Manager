import random
import hashlib
import pyperclip
import sys
import mysql.connector

possible = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890;'/.,<>?:\"/\\!@#$%^&*()_+-=`~")

## generating funtion
def generate(length):
    global password
    password = ""
    for i in range(length):
        password+=random.choice(possible)
    print("Your Generated password is : " + password)
    return password

def hashing_password(FOR_hash_password):
    ## Hashing Password
    hash = hashlib.md5()
    hash.update(FOR_hash_password.encode('utf-8'))
    global hash_password
    hash_password = hash.hexdigest()
    global note
    note = input("Any additnoal NOTE[Default:NONE] : " or "NONE")
    save_passwd_db()


## Choice
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
        hashing_password(password) ## This Will call the fuction to hash the password
        sys.exit()
    elif (choice == 2):
        print("---------------------------------")
        print("Regenrating Your password....")
        password = generate(length)
        choice_fun(password)
    else:
        print("Enter a valid choice")
        choice_fun(password)



### Databases connection
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "pass_admin", passwd = "Pass00Qwas@121", database = "pass_manager")

## Checking Connection  
if conn.is_connected() == False:
    print ( "error while connecting to mysql database")
else:
    print ("mysql database is connected successfully")

## setting up cursor to run commands
cursor = conn.cursor()

## user input
# password_hash = input("Enter password hash to save in database : \n")

def save_passwd_db():
    ## Command Execution 
    cursor.execute(f"insert into passwords values('{site}', '{hash_password}', '{note}');")
    conn.commit()
    conn.close()

def view_saved_pass():
    ## search query
    search = input("Enter key phrase : ")
    cursor.execute(f'''select site_name, passwd from passwords where site_name like '%{search}%' or site_name like '%{search}' or site_name like '{search}%' or site_name like '{search}' or note like '%{search}%' or note like '%{search}' or note like '{search}%' or note like '{search}';''')
    data = cursor.fetchall()
    # print(data)
    for row in data:
        print(row)
    conn.close()



## main function

def main_menu():
    choice = int(input('''1). Generate new password
2). View saved passwords
Enter Your Choice : '''))
    if (choice == 1 ):
        global site
        site = input("Enter the site name for which you're saving the password : ")
        global length
        length = int(input('''Enter the length of your password (RECOMMENDED[9-16])
        (Default[11] : ''') or "11")
        password =  generate(length)
        choice_fun(password)
        
    elif (choice == 2):
        print("---------------------------------")
        view_saved_pass()
    else:
        print("Enter a valid choice")
        main_menu()

main_menu()
