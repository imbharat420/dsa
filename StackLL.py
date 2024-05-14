class Node:
    def __init__(self,item=None,next=None):
        self.next=next
        self.item=item
class Stack:
    def __init__(self,start=None) -> None:
        self.start=start
        self.item_count=0
    def is_empty(self):
        return self.start == None
        # return self.item_count ==0
    def push(self,item):
        if not self.is_empty(): 
            n=Node(item,self.start)
            self.start=n
            self.item_count+=1
            return n.item
    def pop(self):
        if not self.is_empty():
             data=self.start.item
             self.start=self.start.next
             self.item_count-=1
             return data
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return self.item_count
    