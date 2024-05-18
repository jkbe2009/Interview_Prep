class Node:
  def __init__(self, d):
    self.data = d
    self.left = None
    self.right = None


def find_height_tree(root):
  if root == None:
    return 0
    
  return max(find_height_tree(root.left), find_height_tree(root.right)) + 1
  

def find_nodes_at_k_distance(root, k):
  if root == None:
    return
  
  if k == 0:
    print(root.data, end=" ")
    return
    
  find_nodes_at_k_distance(root.left, k-1)
  find_nodes_at_k_distance(root.right, k-1)
  
  return


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("\n\n")
print("Tree height: ",find_height_tree(root))
print("Nodes at k: ")
find_nodes_at_k_distance(root, 2)