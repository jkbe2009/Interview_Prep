
def is_subsequence(s1, s2):
  if len(s2) > len(s1):
    return False
  i, j = 0, 0
  while i < len(s1) and j < len(s2):
    if s1[i] == s2[j]:
      j = j+1
    i = i+1
  return j == len(s2)
    
def is_subsequence_quick(s1, s2):
  if len(s2) > len(s1):
    return False

  start = 0
  index = -1

  for char in s2:
    index = s1.find(char, start)
    if index == -1:
      return False
    start = index+1
  return True

s1 = "GEEKSFORGEEKS"
s2 = "GRGES"
#s2 = "ADE"

print(is_subsequence_quick(s1, s2))
print(is_subsequence(s1, s2))
# O(m+n) || O(1)
