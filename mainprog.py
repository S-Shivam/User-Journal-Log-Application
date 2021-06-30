import datetime
import os
import sys
import codecs
import getpass
import pathlib


option = ""
###Start up menu
def start_menu(option):
    if option == "1" or option == 1:
        login()
    elif option == "2" or option == 2:
        signup()
    elif option == "3" or option == 3:
        sys.exit()
    else:
        print("Please enter correct choice")
        sys.exit()

###User Login
def login():
    user = input("Username: ")
    password = getpass.getpass(prompt='Password: ')

    cwd = os.getcwd()
    
    path = cwd + "/Users"
    
    filename = path + "/" + user.replace(" ","") + ".bin"

    file = pathlib.Path(filename)
    if file.exists():
        with open(filename, 'rb') as entry:
            lines = entry.read()
            test = codecs.decode(lines, "hex")
            pwd = test.decode("utf-8")
        if password == pwd:
            operations()
        else:
            print("Invalid Password")
            sys.exit()
    else:
        print("Username does not exists")
        sys.exit()

    
###New User SignUp        
def signup():

    user = input("Enter a Unique Username: ")

    cwd = os.getcwd()
    
    path = cwd + "/Users"
    try:  
        os.mkdir(path)
    except OSError:  
        print (" ")
        
    filename = path + "/" + user.replace(" ","") + ".bin"

    file = pathlib.Path(filename)
    
    if file.exists():
        print("Username already exists")
        signup()
    else:
        name = input('Enter your name: ')
        password = getpass.getpass(prompt='Password: ')

        data = bytes(password,'ascii')
        hexStr = codecs.encode(data, 'hex')
        with open(filename, 'ab') as entry:
            entry.write(hexStr)
        operations()

###Journal Creation        
def create_journal():
    
    cwd = os.getcwd()
    
    path = cwd + "/Journal"    

    try:  
        os.mkdir(path)
    except OSError:  
        print (" ")
        
    add_entry(path)

####Adding New Entry to the Journal
def add_entry(path):
    title = input("Enter name for your journal:   ")
    content = get_entry()
    filename = path + "/" + title.replace(" ","") + ".bin"
    
    line = str(datetime.datetime.now()) + " - " + str(content) + "  "
    data = bytes(line,'ascii')
    hexStr = codecs.encode(data, 'hex')
    with open(filename, 'ab') as entry:
        entry.write(hexStr)

###Opening a Journal    
def open_journal():
    name = input("Enter name of your journal:  ")
    cwd = os.getcwd()
    filename = cwd + "/Journal/" + name + ".bin"

    file = pathlib.Path(filename)
    
    if file.exists():
        with open(filename, 'rb') as entry:
            lines = entry.read()
            data = codecs.decode(lines, "hex")
        print("All previous Entries: ")
        print(data.decode("utf-8"))
    else:
        print("Journal Not found")
        operations()

###Get Journal Entry from the User   
def get_entry():
    content = input("Write your journal's entry:  ")
    return content

###Operations for Journal Management
def operations():
    print("Operations: ")
    print("1: List Journal entries")
    print("2: Create a new entry")
    option = input("Enter your choice:  ")
    
    if option == "1" or option == 1:
        open_journal()
    elif option == "2" or option == 2:
        create_journal()
    else:
        print("Please enter correct choice")
        operations()

    choice = input("Do you want to continue?(y/n)")
    if choice == "y" or choice == "yes":
        operations()
    else:
        sys.exit()

print("1: Login")
print("2: Sign Up(New User)")
print("3: Exit")
option = input("Enter choice:  ")
start_menu(option)
