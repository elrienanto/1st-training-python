def XO():
    a = input("s")
    if (a.lower().count('o')) == (a.lower().count('x')) or ((a.lower().count('o')) and (a.lower().count('o')) == 0):
             return True
    else:
            return False

    Print (XO)