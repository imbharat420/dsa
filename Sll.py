"""Singly Linked List"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self):
        self.start = None
    def is_empty(self)-> bool:
        return self.start is None 
    def insert_at_start(self,data):
        node = Node(data,self.start)
        self.start = node
    def insert_at_end(self,data):
        node = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
           node = Node(data,temp.next)
           temp.next = node
    def print_list(self):
        temp = self.start 
        while temp is not None:
            print(temp.item) 
            temp = temp.next
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        
l1 = SLL()
l1.insert_at_start(30)
l1.insert_at_end(49)
l1.insert_at_end(59)
l1.insert_at_end(69)
l1.insert_after(l1.search(59),33)
l1.print_list()

#chk = l1.search(49)
#print(chk)