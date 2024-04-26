class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
class CDll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start == None 
    def insert_at_start(self,data):
        n=Node(data,self.start.prev,self.start)
        self.start=n