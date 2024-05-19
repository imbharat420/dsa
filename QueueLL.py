class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self,item):
        n=Node(item)
        if self.is_empty():    
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
           raise IndexError("Queue is empty")
        elif self.rear==self.front:
            self.rear=None
            self.front=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
           raise IndexError("Queue is empty")
        return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.rear.item
    def size(self):
        return self.item_count
    
cls=Queue()
cls.enqueue(20)
cls.enqueue(40)
cls.enqueue(60)
cls.enqueue(80)
cls.dequeue()
# cls.dequeue()
# cls.dequeue()
print(cls.size())
print("front",cls.get_front(),":  rear",cls.get_rear())