def reverse_string(s):
  # Edge case:
  if s is None:
    raise ValueError("Invalid input: None!!!")
  if len(s) < 1:
    return s

  input = list(s) # Convert to a list to perform in place reversal

  l, r = 0, len(input)-1

  while l < r:
    input[l],input[r] = input[r],input[l]
    l += 1
    r -= 1
  
  return ''.join(input)


def reverse_string_preserve_spacing(s):
  # Edge case:
  if s is None:
    raise ValueError("Invalid Input!!!")
  if len(s) <= 1:
    return s

  input = list(s)
  l, r = 0, len(input)-1
  
  while l < r:
    while (input[l] == ' '):
      l += 1
    while (input[r] == ' '):
      r -= 1
    input[l], input[r] = input[r], input[l]
    l += 1
    r -= 1
  
  return ''.join(input)
  

def reverse_vowel(s):
  # Edge case:
  if s is None:
    raise ValueError("Invalid Input!!!")
  if len(s) <= 1:
    return s
  # Vowel set for checking
  vowel = {'a','e','i','o','u','A','E','I','O','U'}

  input = list(s)
  l, r = 0, len(input)-1

  while l < r:
    while (input[l] not in vowel):
      l += 1
    while (input[r] not in vowel):
      r -= 1
    input[l], input[r] = input[r], input[l]
    l += 1
    r -= 1

  return ''.join(input)
  
  

print(reverse_string("karthik"))
print(reverse_string_preserve_spacing("I work at Google"))
print(reverse_vowel("A man is walking!"))