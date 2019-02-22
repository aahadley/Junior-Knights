# Aaron Hadley
# February 22, 2019

def login(username, password, database):

    while not(username in database):
        print("username not found")
        username = input("Enter your username\n\t")
        password = input("Enter your password\n\t")
        
    if database[username] == password:
        print("login successful!")
        return True

    else:
        return False


def register(username, password, database):

    database[username] = password
    login(username, password, database)


database = {}
 
while True:
    choice = int(input("1. Login\n2. Register\n3. Exit\n\t"))
    username = input("Enter your username:\n\t")
    password = input("Enter your passsword:\n\t")


    if choice == 1:
        login(username, password, database) == True:
            
    if choice == 2:
        register(username, password, database)
    
    if choice == 3:
        return 0