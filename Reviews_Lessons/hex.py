import random

user_input = int(input("Enter a number.\n"))
input_o = user_input
output = []

hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

while(True):
    output.insert(0, hex_digits[user_input % 16])
    user_input //= 16

    if(user_input <= 0):
        break
    
print(hex(input_o))
print("0x" + ''.join(output))