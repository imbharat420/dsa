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
            root.left = self.rinsert(root.left)
        elif data > root.item:
            root.right = self.rinsert(root.left)
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
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(self.left,result)
            self.rpreorder(self.right,result)

    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(self.left,result)
            self.rpostorder(self.right,result)
            result.append(root.item)
        