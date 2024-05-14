class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,item):
        n=Node(item,self.start)
        self.start=n
    def insert_at_end(self,item):
        n=Node(item)
        if self.start is None:
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,item):
        if temp is not None:
            n=Node(item,temp.next)
            temp.next=n
    def delete_first(self):
        if not self.is_empty():
            self.start=self.start.next
    def delete_last(self):
        if self.is_empty():  # if empty
            pass
        elif self.start.next is None: # if only one element
            self.start=None
        else:  # if more than 1 element
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        
            
    def delete_after(self,data):
        if self.is_empty():
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else: 
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                while temp is not None:
                    if temp.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                    
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
# cls=SLL()
# cls.insert_at_start(10)
# cls.insert_at_start(20)
# cls.insert_at_start(30)
# cls.insert_at_end(80)
# cls.insert_at_start(90)
# cls.insert_after(cls.search(80),33)
# cls.delete_first()
# cls.delete_after(10)
# cls.print_list()
