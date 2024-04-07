class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next 

class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,item):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next!=None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                 temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
    def delete_start(self): 
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev= None
    def delete_last(self):
        if self.is_empty():
            pass
        elif self.start.next is None:
            self.start = None
        elif self.start!=None:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_item(self,data):
        if self.is_empty():
            pass
        else:
            temp =self.start
            while temp is not None:
                if temp.item is not None:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next