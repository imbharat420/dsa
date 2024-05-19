# We Append rear and front is in 0 index
class Deque:
    def __init__(self):
        self.items=[]
        # self.front=None
        # self.rear=None
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,item):
        return self.items.insert(0,item)
    def insert_rear(self,item):
        return self.items.append(item)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.items.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.items.pop()
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[-1]
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[0]
    def size(self):
        return len(self.items)

cls=Deque()
cls.insert_front(20)
cls.insert_front(21)
cls.insert_front(23)
cls.insert_rear(29)
cls.insert_rear(29)
cls.insert_rear(39)

print("size",cls.size(),"front",cls.get_front(),":  rear",cls.get_rear())