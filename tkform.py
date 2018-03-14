from tkinter import Frame,Button,Tk

class Application(Frame):
    def SayHi(self):
        print("Hi there, everyone")

    def CreateWidgets(self):
        self.QUIT = Button(self)
        self.QUIT['text'] = "quit"
        self.QUIT['fg'] = 'red'
        self.QUIT['command'] = self.quit
        self.QUIT.pack({'side':'left'})

        self.hi = Button(self)
        self.hi['text'] = 'Say Hi'
        self.hi['fg'] = 'blue'
        self.hi['command'] = self.SayHi()
        self.hi.pack({'side':'right'})

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.CreateWidgets()
root=Tk()
root.title("Hello")
root.geometry('400x400')
app = Application(master = root)
app.mainloop()
root.destroy()