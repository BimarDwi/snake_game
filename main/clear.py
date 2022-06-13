import os


def clear():
    if os.name == "nt":     # windows
        os.system("cls")
    else:                   # linux and mac
        os.system("clear")
