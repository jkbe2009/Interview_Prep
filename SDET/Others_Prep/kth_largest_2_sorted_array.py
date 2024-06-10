
def kth_largest(l1, l2, k):
  i, j = 0, 0
  n, m = len(l1), len(l2)
  counter = 0
  
  while i < n and j < m:
    if l1[i] < l2[j]:
      if n+m-counter == k:
        return l1[i]
      i += 1
      counter += 1
    else:
      if n+m-counter == k:
        return l2[j]
      j += 1
      counter += 1
      
  while i < n:
    if n+m-counter == k:
      return l1[i]
    i += 1
    counter += 1
  while j < m:
    if n+m-counter == k:
      return l2[j]
    j += 1
    counter += 1
  
  return -1



arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 10
print(sorted(arr1+arr2))
print(kth_largest(arr1, arr2, k))