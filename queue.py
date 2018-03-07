class Queue:
    def __init__(self):
        self.queue = []
        self.r = 0
        self.f = 0
    
    def Insert(self,ele):
        self.queue.append(ele)
        self.r += 1
    
    def Delete1(self):
        if self.r == self.f:
            print("Queue Underflow")
            return
        print("Deleted Element =", self.queue[self.f])
        self.f+=1

    def QueueFront(self):
        if self.r == self.f:
            print("Queue Underflow")
            return
        print("Front element of Queue =",self.queue[self.f])
    
    def Display(self):
        if self.r == self.f:
            print("Queue empty")
            return
        for i in range(self.f,self.r-1):
            print(self.queue[i],end=", ")
        print(self.queue[self.r-1])

queue1 = Queue()
while True:
    ch = input("insert, delete, qf, display, exit :")
    if ch == 'exit':
        break
    if ch == 'insert':
        ele = input("Give element: ")
        queue1.Insert(ele)
        queue1.Display()
    elif ch == 'delete':
        queue1.Delete1()
        queue1.Display()
    elif ch == 'qf':
        queue1.QueueFront()
        queue1.Display()
    elif ch == 'display':
        queue1.Display()