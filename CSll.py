class Node:
    def __init__(self,item=None,next=None):
        self.next=next
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
    def insert_after(self,temp,item):
        if temp is not none:
            n=Node(item,temp.next)
            temp.next=n
            if temp == self.last:
                self.last=n  
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp != self.last:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item) #This because self.last is in 1st position or in last Position when loop is false
    def delete_first(self):    
        if not self.is_empty():
            if self.last.next == self.last
                self.last = None
            else:
                self.last.next = self.last.next.next
    def delete_last(self):    
        if not self.is_empty():
            if self.last.next == self.last
                self.last = None
            else:
                temp = self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.item == data:
                self.last = None
            else:
                if self.last.next.item == data:
                    return self.delete_first()
                
                temp=self.last.next 
                while temp!=self.last:
                    if temp.next == self.last:
                        if self.last.item == data:
                         self.delete_last()
                         break
                    if temp.item == data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next