
#range(start, stop, step)
'''
l = list(range(1, 101))

newlist = []

for i in range (24, 30):
    newlist.append(l[i])

newlist = l[1::2]

print(newlist)


for i in l[1::2]:
    print(i**2)

l1 = [i**2 for i in range(0, 101, 2)]

print(l1)
'''

'''

# sets
l = [2, 2, 2, 3, 4, 6, 8]
s = {2}

l= list(set(l))
print(l)
'''
'''
d = {1:"Aaron", 2:"Tim", "thisguy":"Diego"}

print( d["thisguy"] )
'''
'''
database = {"minecraftlover44":"1234", "xxcodfan22":"4321", "epicgamer":"abcd"}

username = input("Enter your username:\n\t")
password = input("Enter your passsword:\n\t")

if username not in database:
    print("invalid username")
    exit()

if database[username] == password:
    print("login successful")

else:
    print("login failed.")
'''

database = {}
def login(username, password, database):
    print("login")
    print(database)
    while not(username in database):
        print("username not found")
        username = input("Enter your username")
        password = input("Enter your password")
        

    if database[username] == password:
        print("login successful")
        return True

    else:
        return False


def register(username, password, database):

    database[username] = password
    login(username, password, database)
    print(database, "at register")


while True:
    choice = int(input("1. Login\n2. Register\n\t"))
    username = input("Enter your username:\n\t")
    password = input("Enter your passsword:\n\t")

    if choice == 1:
        if login(username, password, database) == True:
            break
            

    if choice == 2:
        register(username, password, database)




