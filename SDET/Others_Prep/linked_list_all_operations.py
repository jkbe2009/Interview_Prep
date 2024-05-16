"""

0. print all items in list
1. insert at first
2. insert at last
3. insert at any pos
4. delete at first
5. delete at last
6. delete at any pos
7. delete a node matching a value
8. sorted insert linked list
9. find the middle of list
10. n node from end of list
11. remove duplicates from sorted list

"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


def print_list(head):
  if head is None:
    print("Empty list !!!")
    return

  curr = head

  while curr:
    print(curr.data, end="")
    curr = curr.next
    if curr != None:
      print(" -> ", end="")
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
  if head == None:
    return temp

  curr = head

  while curr.next != None:
    curr = curr.next
  curr.next = temp
  return head


def insert_at_pos(head, key, pos):
  temp = Node(key)
  if head == None and pos <= 0:
    print("Invalid Input")
    return None  
  
  if pos == 1 or head == None:
    temp.next = head
    return temp
    
  curr = head
  count = 2
  while curr.next != None and count < pos:
    curr = curr.next
    count = count+1

  if count < pos:
    print("Invalid Input, the insert position is beyond the list")
    return head
  temp.next = curr.next
  curr.next = temp  
  return head


def delete_at_first(head):
  if head == None:
    return None
  return head.next


def delete_at_last(head):
  if head == None or head.next == None:
    return None
  
  curr = head
  while curr.next.next != None:
    curr = curr.next
  curr.next = curr.next.next
  return head

  
def delete_at_pos(head, pos):
  if head == None:
    return None
  if pos == 1:
    return head.next
  curr = head
  count = 2
  while curr.next.next != None and count < pos:
    curr = curr.next
    count = count+1
  if count < pos:
    print("Invalid Input, the delete position is beyond the list")
    return head 
  curr.next = curr.next.next
  return head


def delete_node_value(head, key):
  if head == None:
    return None
  if head.next == None:
    if head.data == key:
      return head.next
    else:
      print("The node is not found in the list")
      return head  
    
  curr = head
  while curr.next.next != None and curr.next.data != key:
    curr = curr.next
  if curr.next.data != key:
    print("The node is not found in the list")
    return head
  curr.next = curr.next.next    
  return head


def sorted_insert(head, key):
  temp = Node(key)
  if head == None:
    return head
  if head == None or key <= head.data:
    temp.next = head
    return temp
    
  curr = head

  while curr.next != None and curr.next.data < key:
    curr = curr.next
  temp.next = curr.next
  curr.next = temp

  return head


def find_middle_node(head):
  if head == None or head.next == None:
    return head
    
  slow = head
  fast = head

  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
  return slow.data


def find_n_node_from_end(head, n):
  if head == None or n <= 0:
     return -1
  slow, fast = head, head

  for i in range(n):
    if fast == None:
      print("Invalid nth position, It exceeds the length of the list")
      return -1
    fast = fast.next
    
  while fast != None:
    fast = fast.next
    slow = slow.next

  return slow.data


def remove_duplicates_sorted_list(head):
  if head == None or head.next == None:
    return head
  
  prev = head
  curr = head.next

  while curr != None:
    if curr.data != prev.data:
      prev.next = curr
      prev = curr
    curr = curr.next
  prev.next = None
  return head



# print_list(None)
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# head = None
print_list(head)
head = insert_at_first(head, 1)
print_list(head)
head = insert_at_last(head, 2)
print_list(head)
head = insert_at_pos(head, 3, 5)
print_list(head)
head = insert_at_pos(head, 3, 10)
print_list(head)
head = delete_at_first(head)
print_list(head)
head = delete_at_last(head)
print_list(head)
head = delete_at_pos(head, 3)
print_list(head)
head = delete_node_value(head, 20)
head = delete_node_value(head, 3)
head = delete_node_value(head, 25)
print_list(head)
head = insert_at_last(head, 20)
head = insert_at_last(head, 30)
head = insert_at_last(head, 40)
head = insert_at_last(head, 50)
head = insert_at_last(head, 60)
print_list(head)
head = sorted_insert(head, 55)
print_list(head)
print(find_middle_node(head))
print_list(head)
print(find_n_node_from_end(head, 2))
head = insert_at_first(head, 10)
head = insert_at_first(head, 10)
head = insert_at_last(head, 60)
head = insert_at_last(head, 60)
head = insert_at_pos(head, 40, 6)
head = insert_at_pos(head, 40, 7)
print_list(head)
remove_duplicates_sorted_list(head)
print_list(head)