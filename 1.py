"""
    Check to see if a string has the same amount of 'x's and 'o's. 
    The method must return a boolean and be case insensitive. 
    The string can contain any char.
"""

def XO(s):
        return s.lower().count('o') == (s.lower().count('x')) or (s.lower().count('o') and (s.lower().count('o')) == 0)

print(XO("ooxx")) # true
print(XO("xooxx")) # false
print(XO("ooxXm")) # true
print(XO("zpzpzpp")) # true // when no 'x' and 'o' is present should return true
print(XO("zzoo")) # false