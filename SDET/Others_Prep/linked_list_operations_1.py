class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def print_linked_list(head):
  if head == None:
    return

  curr = head

  while curr != None:
    print(curr.data, end ="")
    curr = curr.next
    if curr != None:
      print(" -> ", end ="")
  print("")
  return

def find_item(head, item):
  if head == None:
    return -1

  pos = -1
  counter = 1
  curr = head

  while curr != None:
    if curr.data == item:
      pos = counter
      break
    curr = curr.next
    counter = counter+1
  return pos

def insert_at_first(head, key):
  temp = Node(key)
  temp.next = head
  return temp

def insert_at_last(head, key):
  temp = Node(key)
  # Edge case:
  if head == None:
    return temp
  # Go to the last element in the LL
  curr = head
  while curr.next != None:
     curr = curr.next
  # curr points to the last element
  curr.next = temp
  return head

head = Node(10)
# head = None
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Linked List operations")
print_linked_list(head)
print("Finding element")
print("Find element 50 :", find_item(head, 50))
print("Find element 40 :",find_item(head, 40))
print("Inserting element at the beginning")
head = insert_at_first(head, 3)
print_linked_list(head)
head = insert_at_first(head, 2)
print_linked_list(head)
head = insert_at_first(head, 1)
print_linked_list(head)
print("Inserting element at the end")
head = insert_at_last(head, 4)
print_linked_list(head)
head = insert_at_last(head, 5)
print_linked_list(head)