

def union_sorted_list(a, b):
  c = []

  aptr, bptr, cptr  = 0, 0, 0

  while aptr < len(a) and bptr < len(b):
    if a[aptr] == b[bptr]:
      val = a[aptr]
      c.append(val)
      while (aptr < len(a) and a[aptr] == val):
        aptr = aptr+1
      while (bptr < len(b) and b[bptr] == val):
        bptr = bptr+1
      continue

    if a[aptr] < b[bptr]:
      c.append(a[aptr])
      aptr = aptr+1

    else:
      c.append(b[bptr])
      bptr = bptr+1

  while aptr < len(a):
    val = a[aptr]
    c.append(val)
    while (aptr < len(a) and a[aptr] == val):
      aptr = aptr+1

  while bptr < len(b):
    val = b[bptr]
    c.append(val)
    while (bptr < len(b) and b[bptr] == val):
      bptr = bptr+1

  return c



a = [2, 3, 3]
b = [3, 4, 4]
print(union_sorted_list(a, b))