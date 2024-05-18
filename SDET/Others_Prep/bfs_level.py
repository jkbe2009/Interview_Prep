from collections import deque

class Node:
  def __init__(self, d):
    self.data = d
    self.left = None
    self.right = None


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

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("\nPreorder Traversal:")
dfs_preorder(root)
print("\n\nInorder Traversal:")
dfs_inorder(root)
print("\n\nPostorder Traversal:")
dfs_postorder(root)
print("\n\nLevelorder Traversal:")
bfs(root)