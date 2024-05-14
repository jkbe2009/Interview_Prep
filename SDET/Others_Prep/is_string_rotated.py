
def is_rotated(s1, s2):
  if len(s1) != len(s2):
    return False
    
  mapping = {}
  for i in range(len(s1)):
    mapping[s1[i]] = s1[(i+1)%len(s1)]

  for i in range(len(s2)):
    if (s2[i] not in mapping) or (mapping[s2[i]] != s2[(i+1)%len(s2)]):
      return False

  return True


def is_rotated_quick(s1, s2):
  if(len(s1) != len(s2)):
    return False

  all_rotated_combinations = s1+s1
  
  return s2 in all_rotated_combinations



s1 = "ABCD"
s2 = "DABC"

print(is_rotated(s1, s2))
print(is_rotated_quick(s1, s2))
# O(n) || O(n)
