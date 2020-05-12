from tkinter import *


class Window(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.master.title('Nice GUI v3')
        self.master.geometry('600x600+700+25')
        self.master.columnconfigure([0, 2], weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.config(bg='#fff')
        #self.master.resizable(0, 0)
        self.AddWidgets()


##############################################################################
    ## Component Construster
    def AddWidgets(self):
        # General colours
        white = '#fff'
        grey = '#f0f0f0'
        mainBG = '#27b376'
        ABCol = '#f9a73e'
        # RGB input colours
        redBG = '#bf212f'
        greenBG = '#006f3c'
        blueBG = '#264b96'

        self.TopFrame = Frame(self.master, bg = mainBG, width = 600, height = 150)
        self.TopFrame.grid(column = 0, row = 0, columnspan = 3, sticky = 'new')

        self.BottomFrame = Frame(self.master, bg = mainBG, width = 600, height = 250)
        self.BottomFrame.grid(column = 0, row = 2, columnspan = 3, sticky = 'sew')
        self.BottomFrame.columnconfigure(0, weight=1)
        self.BottomFrame.rowconfigure(0, weight=1)


        self.RFrame = Frame(self.master, bg = white)
        self.RFrame.grid(column = 0, row = 1, padx = 0, pady = 30)
        self.AddRedSection(white, ABCol, redBG)

        self.GFrame = Frame(self.master, bg = white)
        self.GFrame.grid(column = 1, row = 1, padx = 0, pady = 30)
        self.AddGreenSection(white, ABCol, greenBG)

        self.BFrame = Frame(self.master, bg = white)
        self.BFrame.grid(column = 2, row = 1, padx = 0, pady = 30)
        self.AddBlueSection(white, ABCol, blueBG)


    ## Red slider and text box
    def AddRedSection(self, white, ABCol, redBG):
        ## Slider
        self.R = Scale(self.RFrame, from_ = 255, to = 0, bd = 0, bg = redBG , fg = white, highlightbackground = white, sliderrelief = 'flat', activebackground = ABCol, command = self.ColorChange)
        self.R.grid(column = 0, row = 0)
        self.R.set(0)
        ## Text entry
        self.RText = Entry(self.RFrame, bg = redBG, fg = white, relief = 'flat')
        self.RText.grid(column = 0, row = 1)


    ## Green slider and text box
    def AddGreenSection(self, white, ABCol, greenBG):
        ## Slider
        self.G = Scale(self.GFrame, from_ = 255, to = 0, bd = 0, bg = greenBG, fg = white, highlightbackground = white, sliderrelief = 'flat', activebackground = ABCol, command = self.ColorChange)
        self.G.grid(column = 0, row = 0) 
        self.G.set(237)
        ## Text entry
        self.GText = Entry(self.GFrame, bg = greenBG, fg = white, relief = 'flat')
        self.GText.grid(column = 0, row = 1)


    ## Blue slider and text box
    def AddBlueSection(self, white, ABCol, blueBG):
        ## Slider           
        self.B = Scale(self.BFrame, from_ = 255, to = 0, bd = 0, bg = blueBG, fg = white, highlightbackground = white, sliderrelief = 'flat', activebackground = ABCol, command = self.ColorChange)
        self.B.grid(column = 0, row = 0)
        self.B.set(115)
        ## Text entry
        self.BText = Entry(self.BFrame, bg = blueBG, fg = white, relief = 'flat')
        self.BText.grid(column = 0, row = 1)

##############################################################################
    ## Callbacks
    def ColorChange(self, x):
        newC = [self.R.get(), self.G.get(), self.B.get()] 
        newC = self.rgb2Hex(newC)
        self.BottomFrame.config(bg = newC) 



##############################################################################
    ## Helper functions
    def rgb2Hex(self, rgb):
        rgb = [hex(i) for i in rgb]
        out = '#'
        for i in rgb:
            i = i[2:]
            out = out + '{:0>2}'.format(i)
        return out




root = Tk()
window = Window(root)
window.mainloop()
