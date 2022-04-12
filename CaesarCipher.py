# This program is a Caesar Cipher.
# It will encrypt a word by shifting each alphabetic character in the text by a fixed amount.
# This program uses a shift of 4 for each character.
# Random comment

string = input("Enter a word or phrase: ")
alist = list(string)
blist = []

for item in alist:
    if item == "a":
        item = "e"
    elif item == "b":
        item = "f"
    elif item == "c":
        item = "g"
    elif item == "d":
        item = "h"
    elif item == "e":
        item = "i"
    elif item == "f":
        item = "j"
    elif item == "g":
        item = "k"
    elif item == "h":
        item = "l"
    elif item == "i":
        item = "m"
    elif item == "j":
        item = "n"
    elif item == "k":
        item = "o"
    elif item == "l":
        item = "p"
    elif item == "m":
        item = "q"
    elif item == "n":
        item = "r"
    elif item == "o":
        item = "s"
    elif item == "p":
        item = "t"
    elif item == "q":
        item = "u"
    elif item == "r":
        item = "v"
    elif item == "s":
        item = "w"
    elif item == "t":
        item = "x"
    elif item == "u":
        item = "y"
    elif item == "v":
        item = "z"
    elif item == "w":
        item = "a"
    elif item == "x":
        item = "b"
    elif item == "y":
        item = "c"
    elif item == "z":
        item = "d"
    elif item == "A":
        item = "E"
    elif item == "B":
        item = "F"
    elif item == "C":
        item = "G"
    elif item == "D":
        item = "H"
    elif item == "E":
        item = "I"
    elif item == "F":
        item = "J"
    elif item == "G":
        item = "K"
    elif item == "H":
        item = "L"
    elif item == "I":
        item = "M"
    elif item == "J":
        item = "N"
    elif item == "K":
        item = "O"
    elif item == "L":
        item = "P"
    elif item == "M":
        item = "Q"
    elif item == "N":
        item = "R"
    elif item == "O":
        item = "S"
    elif item == "P":
        item = "T"
    elif item == "Q":
        item = "U"
    elif item == "R":
        item = "V"
    elif item == "S":
        item = "W"
    elif item == "T":
        item = "X"
    elif item == "U":
        item = "Y"
    elif item == "V":
        item = "Z"
    elif item == "W":
        item = "A"
    elif item == "X":
        item = "B"
    elif item == "Y":
        item = "C"
    elif item == "Z":
        item = "D"

    else:
        item = item
    blist.append(item)
cipher = "".join(blist)
print(cipher)
