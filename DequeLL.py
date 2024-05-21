class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==None
    def insert_rear(self,item):
        n=Node(item,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def insert_front(self,item):
        n=Node(item,self.front)
        if self.is_empty():
            self.front=n
        else:
            self.front.prev=n
        self.front=n
        self.item_count+=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.rear.item
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return  self.front.item
    def size(self):
        return self.item_count



        


        