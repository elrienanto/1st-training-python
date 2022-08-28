"""
    Check to see if a string has the same amount of 'x's and 'o's. 
    The method must return a boolean and be case insensitive. 
    The string can contain any char.
"""

from re import I


def XO(s):
    countO = 0
    countX = 0

    #while loop

    i = 0
    while i < len(s):
        print(s[i])
        if s.lower()[i] == ("o"):
            countO += 1  
        if s.lower()[i] == ("x"):
            countX += 1
        i += 1

    #for loop

    for i in range (len(s)):
        print(s.lower()[i])
        if s.lower()[i] == ("o"): 
            countO += 1  
        if s.lower()[i] == ("x"):
            countX += 1  


    print (countO)
    print (countX)

    return countO == countX  

print(XO("ooxx")) # true
print(XO("xooxx")) # false
print(XO("ooxXm")) # true
print(XO("zpzpzpp")) # true // when no 'x' and 'o' is present should return true
print(XO("zzoo")) # false