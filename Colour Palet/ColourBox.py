from tkinter import *


class Window(Frame):
    def __init__(self, root, col):
        super().__init__(root)
        self.master = root
        self.master.title('Colour Box')
        self.master.geometry('200x200+1100+125')
        self.config(bg=col)


root = Tk()
window = Window(root, col)
window.mainloop()
