from tkinter import *


class ColourBox(Frame):
    def __init__(self, root, col):
        super().__init__(root)
        self.master = root
        self.master.title('Colour Box')
        self.master.geometry('200x200+1100+125')
        if col is not None:
            self.master.config(bg=col)


def ColourSwob(col):
    root = Tk()
    colourBox = ColourBox(root, col)
    colourBox.mainloop()


def rgb2Hex(rgb):
    rgb = [hex(i) for i in rgb]
    out = '#'
    for i in rgb:
        i = i[2:]
        out = out + '{:0>2}'.format(i)
    return out


if __name__ == '__main__':
    col = '#000000'
    root = Tk()
    colourBox = ColourBox(root, col)
    colourBox.mainloop()
