


grid = [
       ['E', 'A', 'T'],
       ['A', 'A', 'O'],
       ['R', 'U', 'O']
]

words = ["TAE", "EAT", "TA", "TAR", "OOT", "OAE","Z", "AOO", "TAA"]

# O(2^n) || O(2^n)
def find(ind, i, j, dir):
    # Base case:
    if ind == len(word):
       return True

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or word[ind] != grid[i][j]:
       return False
    
    # Recursive case:
    if dir == "L":
       return find(ind+1, i, j-1, "L")
    elif dir == "R":
       return find(ind+1, i, j+1, "R")
    elif dir == "U":
       return find(ind+1, i-1, j, "U")
    elif dir == "D":
       return find(ind+1, i+1, j, "D")
    elif dir == "TR":
       return find(ind+1, i-1, j+1, "TR")
    elif dir == "TL":
      return find(ind+1, i-1, j-1, "TL")
    elif dir == "BR":
       return find(ind+1, i+1, j+1, "BR")
    elif dir == "BL":
       return find(ind+1, i+1, j-1, "BL")

def check(word):
    for i in range(len(grid)):
       for j in range(len(grid[i])):
           ans = (
               find(0, i, j, "L") or\
               find(0, i, j, "R") or\
               find(0, i, j, "U") or\
               find(0, i, j, "D") or\
               find(0, i, j, "TR") or\
               find(0, i, j, "TL") or\
               find(0, i, j, "BR") or\
               find(0, i, j, "BL")
           )
           if ans:
               return True
    return False

for word in words:
   print(check(word))