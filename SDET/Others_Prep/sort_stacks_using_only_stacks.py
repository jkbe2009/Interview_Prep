

def sort_stack(inp):
  res = []
  temp = []

  while inp:
    # Get all the input values one by one
    el = inp.pop()

    # Find the right insertion position
    while res and res[-1] > el:
      temp.append(res.pop())
    # Insert in the correct position on the result stack
    res.append(el)
    # put all the values back into the result
    while temp:
      res.append(temp.pop())
  return res


inp = [2, 10, 3, 6, 7, 5, 9, 1, 4, 8]
print(sort_stack(inp))
