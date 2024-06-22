class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
           return Node(data)
        elif data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root
    def search(self,item):
        return self.rsearch(self.root,item) 
    def rsearch(self,root,item):
        if root is None or root.item == item:
            return root
        elif item < root.item:
            return self.rsearch(self.left,item)
        else:
            return self.rsearch(self.right,item) 
    def inorder(self): #Left -> Root -> Right
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):   # Root -> Left -> Right
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

    def postorder(self): # Left -> Right -> Root
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)

cls = Tree()

cls.insert(20)
cls.insert(10)
cls.insert(40)
cls.insert(50)
cls.insert(100)
print("Inorder   ->",cls.inorder())
print("Preorder  ->",cls.preorder())
print("Postorder ->",cls.postorder())



"""
A Tree Data Structure can be traversed in following ways:

Depth First Search or DFS
Inorder Traversal
Preorder Traversal
Postorder Traversal
Level Order Traversal or Breadth First Search or BFS


Inorder Traversal:
Inorder traversal visits the node in the order: Left -> Root -> Right


Preorder Traversal:
Preorder traversal visits the node in the order: Root -> Left -> Right


Postorder Traversal: 
Postorder traversal visits the node in the order: Left -> Right -> Root

20 - 10 - 40 - 50 - 100

            20
          /   \
         10    40
                \
                 50
                  \
                   100

Inorder   -> [10, 100, 20, 10, 100]   Left -> Root -> Right
Preorder  -> [20, 10, 100, 10, 100]   Root -> Left -> Right
Postorder -> [100, 10, 100, 10, 20]   Left -> Right -> Root

"""