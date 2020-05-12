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
        self.master.resizable(0, 0)
        self.AddWidgets()


##############################################################################
    ## Component Construster
    def AddWidgets(self):
        # General colours
        white = '#fff'
        grey = '#f0f0f0'
        mainBG = '#27b376' # Main background colour
        ABCol = '#f9a73e' # Active background colour
        # The colours for the user input controls
        startColour = (0, 237, 155)
        redBG = '#bf212f'
        greenBG = '#006f3c'
        blueBG = '#264b96'

        self.TopFrame = Frame(self.master, bg = mainBG, width = 600, height = 150)
        self.TopFrame.grid(column = 0, row = 0, columnspan = 3, sticky = 'new')

        self.BottomFrame = Frame(self.master, bg = mainBG, width = 600, height = 250)
        self.BottomFrame.grid(column = 0, row = 2, columnspan = 3, sticky = 'sew')
        
        # Args: X postion, Slider BG colour, _, _, Starting value
        self.RFrame, self.R, self.RText = self.ColourSectionBuilder(0, redBG, ABCol, white, startColour[0])
        self.GFrame, self.G, self.GText = self.ColourSectionBuilder(1, greenBG, ABCol, white, startColour[1]) 
        self.BFrame, self.B, self.BText = self.ColourSectionBuilder(2, blueBG, ABCol, white, startColour[2]) 


    def ColourSectionBuilder(self, xPosIndex, BGColour, ABCol, white, startVal):
        ## The frame
        cBox = Frame(self.master, bg = white)
        cBox.grid(column = xPosIndex, row = 1, padx = 0, pady = 30)

        ## Slider
        # C stands for colour
        C = Scale(cBox, from_ = 255, to = 0, bd = 0, bg = BGColour , fg = white, highlightbackground = white, sliderrelief = 'flat', activebackground = ABCol, command = self.ColorChange)
        C.grid(column = 0, row = 0)
        C.set(startVal)

        ## User text imput
        strvar = StringVar()
        valCmd = (self.register(self.userRGBValidate), '%W')
        CText = Entry(cBox, bg = BGColour, fg = white, relief = 'groove', textvariable = strvar, validate = "key", validatecommand = lambda strvar=strvar: self.userRGBValidate(strvar))
        CText.grid(column = 0, row = 1)
        return Frame, C, CText


##############################################################################
    ## Callbacks
    def ColorChange(self, x):
        newC = [self.R.get(), self.G.get(), self.B.get()] 
        newC = self.rgb2Hex(newC)
        self.BottomFrame.config(bg = newC) 

    def userRGBValidate(self, target):
        print('test')
        print(target.get())
        return True

    def testText(self, x = 1, y = 2):
        print('Ping')


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
