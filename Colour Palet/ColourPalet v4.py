from tkinter import *


class Window(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.master.title('Nice GUI v4')
        self.master.geometry('600x600+700+25')
        self.master.columnconfigure([0, 1, 2], weight=1)
        self.master.rowconfigure([0, 1, 2], weight=1)
        self.master.config(bg='#fff')
        # self.master.resizable(0, 0)
        self.AddWidgets()

    ###########################################################################
    # --- Component Construster
    def AddWidgets(self):
        # General colours.
        self.white = '#fff'
        self.grey = '#f0f0f0'
        self.mainBG = '#27b376'  # Main background colour.
        self.ABGCol = '#f9a73e'   # Active background colour.
        # The colours for the user input controls.
        self.startColour = (39, 179, 118)
        self.redBG = '#bf212f'
        self.greenBG = '#006f3c'
        self.blueBG = '#264b96'

        #######################################################################
        # --- Top Frame
        self.TopFrame = Frame(self.master, bg=self.mainBG, width=600,
                              height=150)
        self.TopFrame.grid(column=0, row=0, columnspan=3, sticky='NEW')

        #######################################################################
        # --- Bottom Frame
        self.BottomFrame = Frame(self.master, bg=self.mainBG, width=600,
                                 height=250)
        self.BottomFrame.grid(column=0, row=2, columnspan=3, sticky='SEW')

        # The hex colour value label.
        self.hexStr = StringVar(self.BottomFrame)
        self.hexStr.set(self.rgb2Hex(self.startColour))
        self.hexLabel = Label(self.master, text=self.hexStr.get(),
                              background=self.hexStr.get())
        self.hexLabel.grid(column=1, row=2)

        #######################################################################
        # --- Colour Sliders
        self.redSlider = ColourSliders(self, self.redBG)
        self.redSlider.grid(column=0, row=1)
        self.redSlider.C.set(self.startColour[0])

        self.greenSlider = ColourSliders(self, self.greenBG)
        self.greenSlider.grid(column=1, row=1)
        self.greenSlider.C.set(self.startColour[1])

        self.blueSlider = ColourSliders(self, self.blueBG)
        self.blueSlider.grid(column=2, row=1)
        self.blueSlider.C.set(self.startColour[2])

    ###########################################################################
    # --- Helper functions
    def rgb2Hex(self, rgb):
        rgb = [hex(i) for i in rgb]
        out = '#'
        for i in rgb:
            i = i[2:]
            out = out + '{:0>2}'.format(i)
        return out


class ColourSliders(Frame):
    def __init__(self, window, BGCol):
        Frame.__init__(self, window.master)
        self.config(bg=window.white)
        self.grid(column=0, row=0, sticky='NSEW')
        self.columnconfigure(0, weight=1)
        self.rowconfigure([0, 1], weight=1)

        # --- Slider
        # C stands for colour.
        self.C = Scale(self, from_=255, to=0, bd=0,
                       command=self.ColorChange)
        self.C.config(sliderrelief='flat', fg=window.white, bg=BGCol,
                      highlightbackground=window.white,
                      activebackground=window.ABGCol)
        self.C.grid(column=0, row=0)

        # --- User text input
        # String Var is used to have somthing that can be passed to the
        # callback.
        strvar = StringVar()
        CText = Entry(self, bg=BGCol, fg=window.white, relief='groove',
                      textvariable=strvar)
        CText.grid(column=0, row=1)
        # Set a call back when the text entry is clicked away from.
        CText.bind("<FocusOut>", lambda event, slider=self.C,
                   strvar=strvar: window.userRGB(event, slider, strvar))
        CText.bind("<Return>", lambda event, slider=self.C,
                   strvar=strvar: window.userRGB(event, slider, strvar))

    #########################################################################
    # --- Callbacks
    def ColorChange(self, x):
        # x is event data that we don't need here.
        # Used by the slider to set the colour of the sample box.
        newC = [window.redSlider.C.get(), window.greenSlider.C.get(),
                window.blueSlider.C.get()]
        newC = window.rgb2Hex(newC)
        window.hexLabel.config(text=newC)
        window.BottomFrame.config(bg=newC)


root = Tk()
window = Window(root)
window.mainloop()
