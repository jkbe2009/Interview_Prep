class Node:
  def __init__(self, d):
    self.data = d
    self.left = None
    self.right = None

def tree_size(root):
  if root == None:
    return 0
  return tree_size(root.left) + tree_size(root.right) + 1

def tree_max_node(root):
  if root == None:
    return float("-inf")
  return max(tree_max_node(root.left), tree_max_node(root.right), root.data)
  
root = None
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("Tree size: ", tree_size(root))
print("Max Node : ", tree_max_node(root))

