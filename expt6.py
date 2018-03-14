class Stack:
    def __init__(self):
        self.stack=[]
        self.tos=-1
    def Pop(self):
        if self.isEmpty():
            return
        self.tos-=1
        print("Popped element =",self.stack[self.tos+1])
    def Push(self,ele):
        self.tos+=1
        self.stack.append(ele)
    def Stack_Top(self):
        if self.isEmpty():
            return
        print("Top of stack =",self.stack[self.tos])
    def Display(self):
        if self.isEmpty():
            return
        for i in range(self.tos,0,-1):
            print(self.stack[i],end=", ")
        print(self.stack[0])
    def isEmpty(self):
        if self.tos == -1:
            print("Stack Underflow.")
            return True
        else:
            return False
        

stack1 = Stack()
while True:
    ch = input("push, pop, stackTop, display, exit :")
    if ch == 'exit':
        break
    if ch == 'push':
        ele = input("Give element: ")
        stack1.Push(ele)
        stack1.Display()
    elif ch == 'pop':
        stack1.Pop()
        stack1.Display()
    elif ch == 'stackTop':
        stack1.Stack_Top()
        stack1.Display()
    elif ch == 'display':
        stack1.Display()
