
# Consider the input is a sorted array else sort the array to optimize the solution. Returns either the index of the key or -1 if not present

def find_first_occ(a, key):

  l, r = 0, len(a)-1
  
  while(l <= r):
    m = (l+r)//2

    if key == a[m]:
      if (m == 0 or a[m] != a[m-1]):
        # if its the first occ
        return m
      else:
         # keep going left to find the first occ
        r = m-1
    elif key < a[m]:
      r = m-1
    else:
      l = m+1
  return -1


def find_last_occ(a, key):
  l, r = 0, len(a)-1

  while(l <= r):
    m = (l+r)//2

    if key == a[m]:
      if (m == len(a)-1 or a[m] != a[m+1]):
        # if its the last occ
        return m
      else:
         # keep going right to find the last occ
        l = m+1
    elif key < a[m]:
      r = m-1
    else:
      l = m+1
  return -1


def find_total_occ(a, key):
  l = find_first_occ(a, key)
  if l == -1:
    return 0
  r = find_last_occ(a, key)

  # Return total occ or count
  return r-l+1

a = [10,10,20,20,20,30,30,40,50,50]
key = 30

print(find_first_occ(a, key))
print(find_last_occ(a, key))
print(find_total_occ(a, key))