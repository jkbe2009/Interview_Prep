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

def insert_at_pos(head, pos, key):
  if head == None or pos <= 0 or (head.next == None and pos > 0):
    print("Invalid Input given !!!")
    return None

  # Edge case: Insert at first position
  if pos == 1:
    temp = Node(key)
    temp.next = head.next
    return temp
    
  counter = 1 # keeps track of the insertion position
  curr = head # curr node points to the insertion position

  while(curr != None and counter < pos):
    prev = curr
    curr = curr.next
    counter = counter+1

  if counter != pos: # Means reached the end i.e insert pos > the size of LL
    print(f"Invalid Insertion position: {pos} which is > size of LL: {counter-1} ")
    return head

  # curr node points to the current insertion postion
  temp = Node(key)
  prev.next = temp
  temp.next = curr

  return head
  



head = Node(10)
# head = None
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Linked List operations")
print_linked_list(head)
print("Insert at positions")
head = insert_at_pos(head, 1, 1)
print_linked_list(head)
head = insert_at_pos(head, 3, 2)
print_linked_list(head)
head = insert_at_pos(head, 6, 3)
print_linked_list(head)
