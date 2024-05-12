
def union_sorted_list(a, b):
  c = []
  i, j, k = 0, 0, 0
  
  while i < len(a) and j < len(b):
    # Move the i pointer to the correct value ignoring duplicates
    while i < len(a)-1 and a[i] == a[i+1]:
      i = i+1

    # Move the j pointer to the correct value ignoring duplicates
    while j < len(b)-1 and b[j] == b[j+1]:
      j = j+1
    
    if a[i] == b[j]:
      c.append(a[i])
      i = i+1
      j = j+1
    elif a[i] < b[j]:
      c.append(a[i])
      i = i+1
    else:
      c.append(b[j])
      j = j+1
  
  # Copy leftover elements from 'a' list
  while i < len(a):
    # Move the i pointer to the last occurence of any character ignoring duplicates
    while i < len(a)-1 and a[i] == a[i+1]:
      i = i+1
    c.append(a[i])
    i = i+1

  # Copy leftover elements from 'b' list
  while j < len(b):
    # Move the j pointer to the last occurence of any character ignoring duplicates
    while j < len(b)-1 and b[j] == b[j+1]:
      j = j+1
    c.append(b[j])
    j = j+1
  
  return c


a = [2, 3, 3, 4, 6, 6]
b = [3, 4, 4, 5, 5, 7]

print(union_sorted_list(a, b))