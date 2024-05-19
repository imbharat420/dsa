class Queue(list):
    def __init__(self):
        self.items=[]
        # self.rear=None
        # self.front=None
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Queue Underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    def size(self):
        return len(self.items)

cls=Queue()
cls.enqueue(10)
cls.enqueue(20)
cls.enqueue(30)
cls.enqueue(40)
cls.enqueue(50)
cls.dequeue()
cls.dequeue()
cls.dequeue()
cls.dequeue()
try:
    print("Front ==",cls.get_front())
    print("Rear ==",cls.get_rear())
    print("Size ==",cls.size())
except IndexError as e:
    print(e.args[0])
