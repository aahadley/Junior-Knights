user_input = int(input("Enter a number.\n"))
a = b = ""

if(user_input % 3 == 0):
    a ="fizz"

if(user_input % 5 == 0):
    b = "buzz"

print(a + b)