
def reverse(a, l, r):
  while l < r:
    a[l], a[r] = a[r], a[l]
    l += 1
    r -= 1
  return
  
def rotate_left(a, k):
  k = k % len(a)
  if k == 0: 
    print(a)
    return 

  res = [0] * len(a) # Create an empty aux array

  i = 0
  for val in a[k:]:
    res[i] = val
    i += 1 
  for val in a[:k]:
    res[i] = val
    i += 1
  print(res)
  return


def rotate_right(a, k):
  k = k % len(a)
  if k == 0: 
    print(a)
    return 

  res = [0] * len(a) # Create an empty aux array

  i = 0
  for val in a[len(a)-k:]:
    res[i] = val
    i += 1
  for val in a[:len(a)-k]:
    res[i] = val
    i += 1
  print(res)


def rotate_left_inplace(a, k):
  k = k % len(a)
  if k == 0: 
    print(a)
    return 

  reverse(a, 0, k-1)
  reverse(a, k, len(a)-1)
  reverse(a, 0, len(a)-1)

  print(a)
  return


def rotate_right_inplace(a, k):
  k = k % len(a)
  if k == 0: 
    print(a)
    return 

  reverse(a, 0, len(a)-k-1)
  reverse(a, len(a)-k, len(a)-1)
  reverse(a, 0, len(a)-1)

  print(a)
  return

def rotate(a):
  # Edge case:
  if a == None or len(a) <= 1:
    return a

  size = len(a)

  print("\n\nRotating left using aux array")
  for k in range(size+1):
    print(f"\nBy {k}")
    rotate_left(a, k)

  print("\n\nRotating right using aux array")
  for k in range(size+1):
    print(f"\nBy {k}")
    rotate_right(a, k)
    
  print("\n\nRotating left in place")
  for k in range(size+1):
    print(f"\nBy {k}")
    rotate_left_inplace(a[:], k) # Send a copy of the array as its in place

  print("\n\nRotating right in place")
  for k in range(size+1):
    print(f"\nBy {k}")
    rotate_right_inplace(a[:], k) # Send a copy of the array as its in place

  return

if __name__ == "__main__":
  a = [1,2,3,4,5]
  rotate(a)