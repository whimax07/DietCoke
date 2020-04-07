from tkinter import *


class Window(object):
    def __init__(self, master):
        self.master = master
        self.master.title('Nice GUI V2')
        self.master.geometry('400x400+700+1')
        self.master.config(bg='#fff')
        self.master.resizable(0, 0)
        self.AddWidgets()

    def AddWidgets(self):
        self.TopFrame = Frame(self.master, bg = '#42f498', width = 400, height = 100)
        self.TopFrame.grid(column = 0, row = 1)

        self.SayHello = Button(self.master, text = 'Say Hello!', width = 10, height = 2, bd = 0, bg = '#42f498', activebackground = '#fff', activeforeground = '#42f498', fg = '#fff', command = self.ShowHelloBox)
        self.SayHello.grid(column = 0, row = 2, padx = 10, pady = 10) 

    def ShowHelloBox(self):
        print('Hi')


app = Tk()
Window = Window(app)
app.mainloop()