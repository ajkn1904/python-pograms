'''Test 6:

1.	Create a binary tree having at least five nodes using class concept, initialization function and user defined print function. (13th week).
2.	Also preorder and inorder this binary tree.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def __repr__(self):
        return repr(self.data)
    
    def add_left(self,node):
        self.left = node
        
    def add_right(self,node):
        self.right = node
    
def Ctree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    
    return two

def Print_preorder(node):
    print(node)
    if node.left:
        Print_preorder(node.left)
    if node.right:
        Print_preorder(node.right)
           
def Print_inorder(node):
    if node.left:
        Print_inorder(node.left)   
    print(node)   
    if node.right:
        Print_inorder(node.right)

root = Ctree()
'''
        2
       /  \
      7    9
     / \
    1   6
     
'''

print("\n\n")
print("Pre Order Traversal : ")
Print_preorder(root)

print("\nIn Order Traversal : ")
Print_inorder(root)
print("\n\n\n")