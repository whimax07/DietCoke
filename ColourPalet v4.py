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
        # self.master.resizable(0, 0)
        self.AddWidgets()

################################################################################
    # --- Component Construster
    def AddWidgets(self):
        # General colours.
        white = '#fff'
        grey = '#f0f0f0'
        mainBG = '#27b376'  # Main background colour.
        ABCol = '#f9a73e'   # Active background colour.
        # The colours for the user input controls.
        startColour = (0, 237, 155)
        redBG = '#bf212f'
        greenBG = '#006f3c'
        blueBG = '#264b96'

        self.TopFrame = Frame(self.master, bg=mainBG, width=600, height=150)
        self.TopFrame.grid(column=0, row=0, columnspan=3, sticky='new')

        self.BottomFrame = Frame(self.master, bg=mainBG, width=600, height=250)
        self.BottomFrame.grid(column=0, row=3, columnspan=3, sticky='sew')

        self.hexStr = StringVar(self.BottomFrame)
        self.hexStr.set(self.rgb2Hex(startColour))
        self.hexLabel = Label(self.master, text=self.hexStr.get(),
                              background=self.hexStr.get())
        self.hexLabel.grid(column=1, row=3)
        
        # Args: X postion, Slider BG colour, _, _, Starting value.
        self.RFrame, self.R, self.RText = self.ColourSectionBuilder(
            0, redBG, ABCol, white, startColour[0])
        self.GFrame, self.G, self.GText = self.ColourSectionBuilder(
            1, greenBG, ABCol, white, startColour[1])
        self.BFrame, self.B, self.BText = self.ColourSectionBuilder(
            2, blueBG, ABCol, white, startColour[2])

    def ColourSectionBuilder(self, xPosIndex, BGColour, ABCol, white, startVal):
        # --- The frame
        cBox = Frame(self.master, bg=white)
        cBox.grid(column=xPosIndex, row=2, padx=0, pady=30)

        # --- Slider
        # C stands for colour.
        C = Scale(cBox, _from=255, to=0, bd=0, bg=BGColour, fg=white,
                  highlightbackground=white, sliderrelief='flat',
                  activebackground=ABCol, command=self.ColorChange)
        C.grid(column=0, row=0)
        C.set(startVal)

        # --- User text input.
        # String Var is used to have somthing that can be passed to the
        # callback.
        strvar = StringVar()
        CText = Entry(cBox, bg=BGColour, fg=white, relief='groove',
                      textvariable=strvar)
        CText.grid(column=0, row=1)
        # Set a call back when the text entry is clicked away from.
        CText.bind("<FocusOut>", lambda event, slider=C,
                   strvar=strvar: self.userRGB(event, slider, strvar))
        CText.bind("<Return>", lambda event, slider=C,
                   strvar=strvar: self.userRGB(event, slider, strvar))
        return Frame, C, CText

##############################################################################
    # --- Callbacks
    def ColorChange(self, x):
        # Used by the slider to set the colour of the sample box
        newC = [self.R.get(), self.G.get(), self.B.get()]
        newC = self.rgb2Hex(newC)
        self.hexLabel.config(text=newC)
        self.BottomFrame.config(bg=newC)

    def userRGB(self, event, slider, strvar):
        # Set the slider value based on the number the user inputted.
        val = strvar.get()
        if val == '':
            return
        try:
            val = int(val)
        except:
            print('Error: User input is not a number. (Check for spaces)')
            return
        if val >= 0 and val <= 255:
            slider.set(val)
            strvar.set('')
        else:
            print("The value you enter needs to be between 0 and 255.")

    def testText(self, x=1, y=2):
        # For testing
        print('Ping')

##############################################################################
    # --- Helper functions
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
