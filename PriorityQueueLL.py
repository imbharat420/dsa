class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0

    def is_empty(self):
        return self.item_count==0

    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1
        self.print_queue()
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is")
        else:
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
    def size(self):
        return self.item_count
    def peak(self):
        return self.start.item
    def print_queue(self):
        temp = self.start
        queue = []
        while temp:
            queue.append(f"({temp.item}, {temp.priority})")
            temp = temp.next
        print("Queue: " + " -> ".join(queue))

cls = PriorityQueue()
# print(cls.is_empty())   
cls.push(1,4)
cls.push(2,5)
# cls.push(3,2)
cls.push(4,6)
cls.push(5,0)
# cls.push(6,6)
# cls.pop()
# cls.pop()
# print(cls.size())
# print(cls.peak())


# while not cls.is_empty():
#     print(cls.pop())
