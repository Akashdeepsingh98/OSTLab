class Node:
    def __init__(self,data=0, nextn = None, prevn = None):
        self.data = data
        self.next = nextn
        self.prev = prevn
    

class LinkedList:
    def __init__(self):
        self.linkedlist = []
        self.beg = None
        self.end = None
        self.count = 0
    
    def Insert_Beg(self):
        prevn = None
        if self.isEmpty():
            nextn = None
        else:
            nextn = self.beg
        data = input("give data: ")
        newnode = Node(data, nextn, prevn)
        self.beg = newnode
        self.count+=1
    
    def Insert_End(self):
        nextn = None
        if self.isEmpty():
            prevn = None
        else:
            prevn = self.end
        data = input("give data: ")
        newnode = Node(data,nextn,prevn)
        self.end = newnode
        self.count+=1
    
    def Delete_Beg(self):
        if self.isEmpty():
            return
        print(self.beg.data)
        self.beg = self.beg.next
        self.count-=1
    
    def Delete_End(self):
        if self.isEmpty():
            return
        print(self.end.data)
        self.end = self.end.prev
        self.count-=1

    def isEmpty(self):
        if self.count == 0:
            print("Linked List is empty")
            return True
        else:
            return False