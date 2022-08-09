'''Test 7:

1.	Create a binary search tree having at least ten nodes using class concept, initialization function and user defined print function. (13th week).
2.	Also preorder and inorder the binary search tree.
'''

class Node:
    def __init__(self, data):
        self.lnode = None
        self.rnode = None
        self.data = data

def insertN(self, node):
    if self is None:
        self = node
    else:
        if self.data > node.data:
            if self.lnode is None:
                self.lnode = node
            else:
                insertN(self.lnode, node)
        else:
            if self.rnode is None:
                self.rnode = node
            else:
                insertN(self.rnode, node)

def Print_inorder(self):
    if not self:
        return
    Print_inorder(self.lnode)
    print(self.data)
    Print_inorder(self.rnode)

def Print_preorder(self):
    if not self:
        return        
    print(self.data)
    Print_preorder(self.lnode)
    Print_preorder(self.rnode)
    
rt = Node(20)
insertN(rt, Node(7))
insertN(rt, Node(25))
insertN(rt, Node(11))
insertN(rt, Node(50))
insertN(rt, Node(15))
insertN(rt, Node(22))
insertN(rt, Node(8))
insertN(rt, Node(5))
insertN(rt, Node(10))

'''
                20
             /     \
            7       25
          /  \      / \
        5    11   22   50
             /  \     
           8    15
            \
            10
'''

print("\n\n\nIn Order Tree:")
Print_inorder(rt)

print("\nPre Order Tree")
Print_preorder(rt)
print("\n")