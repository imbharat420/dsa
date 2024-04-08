class Node:
    def __init__(self,item,last):
        self.last=last
        self.item=item

class CSll:
    def __init__(self,last=None):
        self.last = None
    def is_empty(self):
        return self.last == None
    def insert_at_start(self,item):
        n=Node(item)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=n
            self.last.next=n
    def insert_at_last(self,item):
        n=Node(item)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=n
            self.last.next=n
            self.last=n
    def search(self,item):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp=temp.next
