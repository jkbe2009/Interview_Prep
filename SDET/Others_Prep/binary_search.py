def bsearch_itr(a, key):
  l, r = 0, len(a)-1

  while(l<=r):
    m = int((l+r)/2)

    if key == a[m]:
      return m
    elif key < a[m]:
      r = m-1
    else:
      l = m+1
      
  return -1

def bsearch_rec(a, key, l, r):
  ## Base Case:
  if l == r:
    if key == a[l]:
      return l
    else:
      return -1
    
  ## Recursive Case:
  m = int((l+r)/2)

  if key == a[m]:
    return m
  elif key < a[m]:
    return bsearch_rec(a, key, l, m-1)
  else:
    return bsearch_rec(a, key, m+1, r)
  

def bsearch(a, key):
  print(f"Found the element at index: {bsearch_itr(a, key)} using iterative method")
  print(f"Found the element at index: {bsearch_rec(a, key, 0 , len(a)-1)} using recursive method")
  return

if __name__ == '__main__':
  bsearch([10, 20, 30, 40, 50], 40)