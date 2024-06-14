

pmap = {
  "pixel 5" : "asfs asf as as KEy1 sdfsd  key1 sdff Key2",
  "pixel 4" : "asfs asf as as kEy2 sdfsd  Key3 sdff key3",
  "pixel 6" : "asfs asf as as sdfsd  key1 sdff",
  "pixel 7": "asfs asf as as keY2 sdfsd sdff key3 key2"
}

keyword = ["keY3", "kEy2", "Key1"]

def product(pmap, keyword):
  resmap = {}
  res = []
  for key in keyword:
    for k, v in pmap.items():
      if key.lower() in v.lower():
        count = v.lower().count(key.lower())
        resmap[k] = resmap.get(k, 0) + count

  for k, v in sorted(resmap.items(), key = lambda item : (-item[1], item[0])):
    res.append((k,v))
  """
  for k, v in sorted(resmap.items(), key = lambda item : (-item[1], item[0]), reverse = True):
    res.append((k,v))
  
  for k, v in sorted(resmap.items(), key = lambda item : (-item[1], item[0])):
    res.append((k,v))
  """
  return res

print(product(pmap, keyword))

# [(pixel4, 3), (pixel5, 3), (pixel7, 2), (pixel6, 1)]

