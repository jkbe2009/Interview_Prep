def find_ele(a, key):
  l, r = 0, len(a)-1
  ind = -1
  
  while l <= r:
    m = (l+r)//2
  
    if (key == a[m]):
      return m
    elif a[l] <= a[m]:
      # left side is sorted
      # check if key is present
      if key >= a[l] and key <= a[m]:
        # Go to left side i.e sorted side
        r = m-1
      else:
        # Go to right side
        l = m+1
    else:
      # right side is sorted
      # check if key is present
      if key >= a[m] and key <= a[r]:
        # Go to Right side i.e sorted side
        l = m+1
      else:
        # Go to Left side
        r = m-1
      
  return ind

def reverse(a, l, r):
  while l < r:
    a[l], a[r] = a[r], a[l]
    l += 1
    r -= 1
  return

def rotate_left_inplace(a, k):
  k = k % len(a)

  reverse(a, 0, k-1)
  reverse(a, k, len(a)-1)
  reverse(a, 0, len(a)-1)

  print(a)
  key = 3
  print(f"The element {key} is at the index: ",find_ele(a, key))
  return

a = [1,2,3,4,5]

for k in range(len(a)+1):
  print(f"\nBy {k}")
  rotate_left_inplace(a[:], k) 
