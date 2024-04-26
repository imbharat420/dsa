class Node:
    def __init__(self,item,next=None):
        self.next=next
        self.item=item
    
class CSll:
    def __init__(self,last=None):
        self.last=last 
    def is_empty(self):
        return self.last == None
    def insert_at_start(self,item):
        n=Node(item)
        if self.is_empty():
            self.last=n
            self.last.next=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,item):
        n= Node(item)
        if self.is_empty():
            n.next=self.last
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def print_list(self):
        temp = self.last.next
        while temp != self.last:
            print(temp.item,end=' ')
            temp=temp.next
        print(temp.item,end=' ')
    def search(self,item):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp !=self.last:
            if temp.item == item:
                return temp
            temp = temp.next
        if temp.next == item:
            return temp 
        return None
    def insert_after(self,temp,item):
        if temp is not None:
            n = Node(item,temp.next)
            temp.next=n 
            if temp == self.last:
                self.last = n
    def insert_before(self,temp,item):
        if temp is not None:
            ttemp = temp.next
            while ttemp.next != temp:
                ttemp = ttemp.next
            n = Node(item,ttemp.next)
            ttemp.next=n 
            # if ttemp == self.last:
            #     self.last = n

    def print_list(self):
        temp = self.last.next
        while temp != self.last:
            print(temp.item)
            temp = temp.next
        print(temp.item)
    # def delete_first(self):



cls = CSll()

cls.insert_at_start(20)
cls.insert_at_start(30)
cls.insert_after(cls.search(30),34)
cls.insert_before(cls.search(34),341)
cls.insert_at_last(344)
cls.print_list()