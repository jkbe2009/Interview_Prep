class Node:
  def __init__(self, d):
    self.data = d
    self.left = None
    self.right = None

from collections import deque

def bfs(root):
  if root == None:
    return

  q = deque()

  q.append(root)

  while q:
    node = q.popleft()
    print(node.data, end=" ")
    left = node.left
    right = node.right
    if left:
      q.append(left)
    if right:
      q.append(right)
  return

def bfs_all_leaf(root):
  if root == None:
    return

  q = deque()

  q.append(root)

  while q:
    node = q.popleft()
    if node == None:
      print("None", end=" ")
      continue
    print(node.data, end=" ")
    left = node.left
    right = node.right
    q.append(left)
    q.append(right)
  return


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("\n\nLevelorder Traversal:")
bfs(root)

root_1 = Node(10)
root_1.left = Node(20)
root_1.right = Node(30)
root_1.left.left = Node(40)
root_1.left.right = Node(50)
root_1.right.left = Node(60)
root_1.right.right = Node(70)
root_1.left.right.right = Node(99)
print("\n\nLevelorder Traversal with all leaf nodes:")
bfs_all_leaf(root_1)
