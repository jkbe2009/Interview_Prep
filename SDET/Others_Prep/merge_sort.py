
def merge_sorted_subarray(a, l, m, r):
  # l <= m < r
  left = a[l:m+1]
  right = a[m+1:r+1]
  i, j, k = 0, 0, l
  alen = len(left)
  blen = len(right)
  
  while i<alen and j<blen:
    if left[i] <= right[j]:
      a[k] = left[i] 
      i = i+1
      k = k+1
    else:
      a[k] = right[j]
      j = j+1
      k = k+1

  while i<alen:
    a[k] = left[i] 
    i = i+1
    k = k+1
  while j<blen:
    a[k] = right[j]
    j = j+1
    k = k+1
    
  return

def merge_sort(a, l, r):
  # l <= m < r
  if l < r:
    m =  (l+r)//2
    merge_sort(a, l, m)
    merge_sort(a, m+1, r)
    merge_sorted_subarray(a, l, m, r)
  return

a = [20, 70, 10, 40, 30, 60, 50]
merge_sort(a, 0 , len(a)-1)
print(a)