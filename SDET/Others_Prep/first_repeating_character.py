def first_repeating_char(s):
  # Edge case:
  if s is None:
    raise ValueError("Invalid input!")
  if s == "" or len(s) == 0:
    return -1
  seen = set()
  unique = set()
  duplicate = set()

  for i, char in enumerate(s):
    if char in seen:
      # save the duplicates
      duplicate.add(char)
      if char in unique:
        unique.remove(char)
    else:
      unique.add(char)
    seen.add(char)
  
  for i, char in enumerate(s):
    if char in duplicate:
      return i
      break

  return -1

s = "geeksforgeeks"
#s = "abcd"

print(first_repeating_char(s))