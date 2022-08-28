"""
    You are given a function that should insert an asterisk (*) between every pair of even digits in the given input, and return it as a string. 
    If the input is a sequence, concat the elements first as a string.

    Input:
    The input can be an integer, a string of digits or a sequence containing integers only.

    Output:
    Return a string.

    Examples:
    5312708     -->  "531270*8"
    "0000"      -->  "0*0*0*0"
    [1, 4, 64]  -->  "14*6*4"
"""


def asterisc_it(n): 
    # your code here
    char = ""
    a = ""
    if not isinstance(n, list):
        a = str(n)
    else: 
        for j in n:
            # print (j)
            a += str(j)
    for i in range (len(a)):
        # if isinstance(n, list):
        #     a[i] = str(a[i])
        char += a[i]         
        if i != len(a)-1 and int(a[i]) % 2 == 0 and int(a[i+1]) % 2 == 0:
            char += "*"
          
    return char

      
print(asterisc_it(5312708)) # 531270*8
print(asterisc_it(9682135)) # 96*8*2135
print(asterisc_it(2222)) # 2*2*2*2
print(asterisc_it(1111)) # 1111
print(asterisc_it(9999)) # 9999
print(asterisc_it('0000')) # 0*0*0*0
print(asterisc_it(8)) # 8
print(asterisc_it(2)) # 2
print(asterisc_it(0)) # 0
print(asterisc_it([1, 4, 64, 68, 67, 23, 1])) # 14*6*4*6*8*67231