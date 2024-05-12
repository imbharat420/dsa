class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next= next

class CDll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n 
            self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            n.prev.next=n
            self.start.prev.next=n

    def search(self,data):
        temp=self.start
        if temp is None:
            return None
        elif temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp.next is not temp:
            if temp.item == data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        n=Node(data)
        if temp is not None:
            print(data,self.start.prev.item,data==self.start.prev.item)
            if data == self.start.item:
                self.insert_at_start(data)
            elif data==self.start.prev.item:
                self.insert_at_last(data)
            else:
                n.next=temp.next
                n.prev=temp
                temp.next.prev=n
                temp.next=n
        
    # def print_list(self):
    #     if not self.is_empty():
    #         temp=self.start
    #         while temp.next !=self.start:
    #             print(temp.item,end=' ')
    #             temp=temp.next
    #         print(temp.item)
    
    def print_list(self):
        temp=self.start
        if temp is not None:
            temp=temp.next
            while temp is not self.start:
                print(temp.item,end=' ')
                temp=temp.next

    def delete_start(self):
       if self.start is not None:
            if self.start.next == self.start:   #Agr only 1 element
               self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next 
    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:   #Agr only 1 element
               self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev=self.start.prev.prev
    def delete_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.item == data:
                self.delete_start()
            else:
                temp = temp.next
                while temp is not self.start:
                    if temp.item == data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
    

     
cls = CDll()
# cls.insert_at_start(20)
# cls.insert_at_start(23)
# cls.insert_at_start(2)
cls.insert_at_start(50)

cls.print_list()
  
# cls.delete_item(5)
# cls.insert_after(cls.search(3),55)
print("")
cls.print_list()
print("")
cls.print_list()