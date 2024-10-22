#Random password generator

import random as r
characters = [[str(i) for i in range(0,9)],[str(chr(i)) for i in range(65,91)],[str(chr(i)) for i in range(97,123)],[str(chr(i)) for i in range(33,48)]]
def generate(length):
    password = ""
    if(length<4):
        return None
    if(length<9):
        print("Your password will be too weak")
    i = int(1)
    count = int(1)
    while(i<=length):
        randomLetter = r.choice(r.choice(characters))
        if(count<=int(length**0.5) and (randomLetter in characters[3])):
            password+=randomLetter
            count = count + 1
        else:
            password+=randomLetter
        i = i + 1
    return password
def lines(loop,new = 0):
    for i in range(loop):
        print("-",end="")
    print("\n",end="")
while(1):
    length = int(input("Enter the length (minimum of 4letters) => "))
    while(1):
        password = generate(length)
        lines(len(password))
        print(password)
        lines(len(password))
        loop = input("\nPress enter to regenerate the password (or)\nenter change to change the length (or)\ntype exit to close => ")
        if(loop != ''):
            break
    if(loop != "change".lower()):
        break
