
def find_min_ele(a):
  # Check if its not rotated
  l, r = 0, len(a)-1
  if a[l] <= a[r]:
    return a[0]

  while l < r:
    m = (l+r)//2

    if (m == 0 or a[m] < a[m-1]) and (m == len(a)-1 or a[m] < a[m+1]):
      return a[m]
    elif a[l] <= a[m]:
      # left side is sorted
      # Go to right side
      l = m+1
    else:
      # right side is sorted
      # Go to left side
      r = m-1
  return a[l]



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
  print(f"Minimum element is : ",find_min_ele(a))
  return

a = [1,2,3,4,5]

for k in range(len(a)+1):
  print(f"\nBy {k}")
  rotate_left_inplace(a[:], k) 
