class PriorityQueue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items) == 0
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
        self.printQueue()
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
    def printQueue(self):
        queue=[]
        index=0
        for temp in self.items:
            queue.append(f"({temp[0]}, {temp[1]})")
            index+=1
        print("Queue: " + " -> ".join(queue))
cls = PriorityQueue()
cls.push(10,1)
cls.push(20,3)
cls.push(30,0)
cls.push(40,4)

