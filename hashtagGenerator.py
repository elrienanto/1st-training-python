"""
    The marketing team is spending way too much time typing in hashtags.
    Let's help them with our own Hashtag Generator!

    Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
"""


def generate_hashtag(s):
    #your code here
    char = False
    isUppercase = False
    #string = ""
    if len(s) == 0:
        return char
    if len(s) <= 140:
        char = "#" 
        for i in range (len(s)):
            if i <= len(s)-1: 
                if  s[i] == " ":
                    isUppercase = True
                else:
                    if i == 0:
                        isUppercase = True
                    if isUppercase == True:
                        char += s[i].upper()
                        isUppercase = False
                    else:            
                        char += s[i].lower()
            

    return char

print(generate_hashtag('')) # False 'Expected an empty string to return False'
print(generate_hashtag('Codewars')) # '#Codewars', 'Should handle a single word.'
print(generate_hashtag('Codewars      ')) # '#Codewars', 'Should handle trailing whitespace.'
print(generate_hashtag('Codewars Is Nice')) # '#CodewarsIsNice', 'Should remove spaces.'
print(generate_hashtag('codewars is nice')) # '#CodewarsIsNice', 'Should capitalize first letters of words.'
print(generate_hashtag('CodeWars is nice')) # '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.'
print(generate_hashtag('c i n')) # '#CIN', 'Should capitalize first letters of words even when single letters.'
print(generate_hashtag('codewars  is  nice')) # '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.'
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat')) # False 'Should return False if the final word is longer than 140 chars.'