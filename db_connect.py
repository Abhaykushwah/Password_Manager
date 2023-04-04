import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "pass_admin", passwd = "Pass00Qwas@121", database = "pass_manager")

## Checking Connection 
if conn.is_connected() == False:
    print ( "error while connecting to mysql database")
else:
    print ("mysql database is connected successfully")

## setting up cursor to run commands
cursor = conn.cursor()

# ## user input
# site = input("Enter the site name for which you're saving the password : ")
# password_hash = input("Enter password hash to save in database : \n")
# note = input("Any additnoal NOTE[Default:NONE] : " or "NONE")


## Command Execution 
# cursor.execute('''insert into passwords values("test.com","9q1sr21ba5b28408cef4f84ea3591f8","same as above");''')
# cursor.execute(f"insert into passwords values('{site}', '{password_hash}', '{note}');")
# conn.commit()


## search query
search = input("Enter key phrase : ")
cursor.execute(f'''select site_name, passwd from passwords where site_name like '%{search}%' or site_name like '%{search}' or site_name like '{search}%' or site_name like '{search}' or note like '%{search}%' or note like '%{search}' or note like '{search}%' or note like '{search}';''')
# cursor.execute('''select site_name, passwd from passwords where site_name like '%google%' or site_name like '%google' or site_name like 'google%' or site_name like 'google' or note like '%google%' or note like '%google' or note like 'google%';''')
# cursor.execute("desc passwords;")


# fetch all
# cursor.execute("select * from passwords;")

data = cursor.fetchall()
# print data
for row in data:
    print(row)


conn.close()

