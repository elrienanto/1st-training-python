"""
    ///////////
    diagonAlley
    ///////////
    Function diagonAlley adalah sebuah function yang membentuk tulisan dalam bentuk diagonal dan
    membentuk bingkai kotak seperti pada test cases. function ini akan menerima parameter string, dan
    function ini berfungsi hanya untuk menampilkan.
    [EXAMPLE]
    INPUT: non
    OUTPUT: 
        n-|
        |o|
        |-n
    NOTES:
        - word membentuk diagonal
        - tepi bingkai horizontal disambung dengan -
        - tepi bingkai vertical disambung dengan |
    [RULES]
    1. Ukuran bingkai sesuai dengan panjang karakter yang diberikan.
    2. Minimal panjang karakter yang diinput adalah 3
"""

def diagonAlley(word):
  X = ""
  for r in range (len(word)):
   for c in range (len(word)):
      if r == c:
        X += word[r]      
      elif c == len(word)-1:
        X += "|"
      elif c == 0:
        X += "|"
      else:
        X += "-"
      if c == len(word)-1:
        X += "\n"
      
  print (X)



# TEST CASES

print(diagonAlley('kuroko'))
"""
  k----|
  |u   |
  | r  |
  |  o |
  |   k|
  |----o
"""
print(diagonAlley('non'))
"""
  n-|
  |o|
  |-n
"""

print(diagonAlley('basuke'))
"""
  b----|
  |a   |
  | s  |
  |  u |
  |   k|
  |----e
"""

print(diagonAlley('no'))
# Invalid input