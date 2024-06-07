

class Node(object):
  def __init__(self, val=None):
    self.val = val
    self.next = None
    self.prev = None

class DLL(object):
  def __init__(self):
    self.front = Node(-1)
    self.back = Node(-1)
    self.front.next = self.back
    self.back.prev = self.front

  def print_list(self):
    curr = self.front.next

    while (curr != self.back):
      print(curr.val, end=" ")
      curr = curr.next
      if curr != self.back:
        print("->", end=" ")
    print("")

  def add(self, val):
    front = self.front
    back = self.back
    temp = back.prev
    node = Node(val)
    
    temp.next = node 
    back.prev = node
    node.next = back
    node.prev = temp
    
  def remove(self, val):
    curr = self.front.next

    while (curr != self.back):
      if curr.val == val:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        return val
      curr = curr.next

obj = DLL()
obj.print_list()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.print_list()
print(obj.remove(2))
print(obj.remove(4))
obj.print_list()