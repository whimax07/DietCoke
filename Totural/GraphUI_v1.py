from tkinter import *
from tkinter.ttk import Notebook

import matplotlib as mpl
import numpy as np
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
mpl.use('TkAgg')


class Window(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.master.title('Plotting Tool')
        self.master.geometry('800x600+700+25')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.AddWigets()

    def AddWigets(self):
        # Set colours here so they can all be change at once.
        buttonColour = '#00c85d'
        self.temp = 0

        # --- Make the "Tab Group" aka Notebook.
        self.tabGroup = Notebook(self.master)
        self.tabGroup.grid(column=0, row=0, sticky='nsew')
        self.tabGroup.columnconfigure(0, weight=1)
        self.tabGroup.rowconfigure(0, weight=1)

        # --- Add the first tab (input).
        self.tab1 = Frame(self.tabGroup)
        self.tabGroup.add(self.tab1, text='Input')

        # Add a label for the first drop down.
        self.dd1Label = Label(self.tab1, text='Choose your favorite Cola:')
        # .grid(..., sticky='w', ...) makes the label stick to the west (left)
        # side of the "area" it has been assigned.
        self.dd1Label.grid(column=0, row=0, sticky='w',
                           padx=(0, 10), pady=(20, 10))

        # Add the first drop down.
        # Get the drop down options.
        dd1List = self.GetList1()
        self.dd1Str = StringVar(self.tab1)
        # Set the option the drop down starts on.
        self.dd1Str.set(dd1List[0])
        self.dd1 = OptionMenu(self.tab1, self.dd1Str, *dd1List)
        # Mess with the look of the drop down this can also change the colour,
        # font size ect.
        self.dd1.config(relief='groove')
        self.dd1.grid(column=1, row=0, sticky='NESW', padx=0, pady=(20, 10))

        # Add a label for the secound drop down.
        self.dd2Label = Label(
            self.tab1, text='Please choose your favorite type of beer:')
        self.dd2Label.grid(column=0, row=1, sticky='w', padx=(0, 10), pady=10)

        # Add the secound drop down.
        dd2List = self.GetList2()
        self.dd2Str = StringVar(self.tab1)
        self.dd2Str.set(dd2List[0])
        self.dd2 = OptionMenu(self.tab1, self.dd2Str, *dd2List)
        self.dd2.config(relief='groove')
        self.dd2.grid(column=1, row=1, sticky='NESW', padx=(0, 10), pady=10)

        # Add the run button.
        # command=self.RunModel executes (aka calls) the function (aka a
        # method of this class) RunModel.
        self.runButton = Button(self.tab1, text='Run', command=self.RunModel)
        self.runButton.config(background=buttonColour, relief='flat')
        self.runButton.grid(column=0, row=2, columnspan=2, padx=0,
                            pady=(40, 0), ipadx=10, ipady=5)

        # --- Add the secound tab (output).
        self.tab2 = Frame(self.tabGroup)
        self.tabGroup.add(self.tab2, text='Output')
        # Controls the resizing of the graph config controls and the graph it
        # self.
        self.tab2.columnconfigure(0, weight=1)
        self.tab2.columnconfigure(0, minsize=250)
        self.tab2.columnconfigure(1, weight=3)
        self.tab2.rowconfigure(0, weight=1)

        # Add two frames to split tab2 to enable spacing of the graph.
        self.Split1 = Frame(self.tab2)
        self.Split1.grid(column=0, row=0, sticky='nesw',
                         padx=(0, 20), pady=0)
        self.Split2 = Frame(self.tab2)
        self.Split2.grid(column=1, row=0, sticky='nesw',
                         padx=(20, 0), pady=0)
        # This enables the resizing behavior of the graph, tab2's config
        # controls the resizing of the left and right side.
        self.Split2.columnconfigure(0, weight=1)
        self.Split2.rowconfigure(0, weight=1)

        # Add a x-axis drop down label.
        self.ddXLabel = Label(self.Split1, text='X-Axis Variable:')
        self.ddXLabel.grid(column=0, row=0, sticky='w',
                           padx=(0, 10), pady=(20, 10))

        # Add a x-axis drop down.
        ddXList = self.GetListX()
        self.ddXStr = StringVar(self.Split1)
        self.ddXStr.set(ddXList[0])
        self.ddX = OptionMenu(self.Split1, self.ddXStr, *ddXList)
        self.ddX.config(relief='groove')
        self.ddX.grid(column=1, row=0, sticky='NESW', padx=0, pady=(20, 10))

        # Add a y-axis drop down label.
        self.ddYLabel = Label(self.Split1, text='Y-Axis Variable:')
        self.ddYLabel.grid(column=0, row=1, sticky='w',
                           padx=(0, 10), pady=(20, 10))

        # Add a y-axis drop down.
        ddYList = self.GetListY()
        self.ddYStr = StringVar(self.Split1)
        self.ddYStr.set(ddYList[0])
        self.ddY = OptionMenu(self.Split1, self.ddYStr, *ddYList)
        self.ddY.config(relief='groove')
        self.ddY.grid(column=1, row=1, sticky='nsew', padx=0, pady=(20, 10))

        # Add a plot button to save dev time.
        # command=self.Plotter executes the function Plotter.
        self.plotButton = Button(self.Split1, text='Plot',
                                 command=self.Plotter)
        self.plotButton.config(background=buttonColour, relief='flat')
        self.plotButton.grid(column=0, row=2, columnspan=2, padx=0,
                             pady=(40, 0), ipadx=10, ipady=5)

        # --- Here we work on the graph.
        # I don't know how to fix the dpi problem.
        f = Figure(figsize=(5, 5), dpi=100)
        self.a = f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(f, self.Split2)
        self.canvas.get_tk_widget().grid(column=0, row=0, sticky='nsew')
        self.canvas.draw()

    def GetList1(self):
        # Replace with a proper import function.
        cokeList = ['Diet Coke', 'Deit Pepsi', "Aldi's Diet Cola"]
        return cokeList

    def GetList2(self):
        # Replace with a proper import function.
        beerList = ['Stout', 'Lager', 'Bitter', 'IPA']
        return beerList

    def RunModel(self):
        # The .get() will pull the value from the drop downs which you can you
        # to set params for the model
        fCoke = self.dd1Str.get()
        fBeer = self.dd2Str.get()
        print('Run model with inputs:', fCoke, 'and', fBeer + '.')

    def GetListX(self):
        # Replace with your x-axis varables if you have them.
        xAxisList = ['Time (s)', 'Distance (m)', 'Temperature (\u00b0C)']
        return xAxisList

    def GetListY(self):
        # Replace with your x-axis varables if you have them.
        yAxisList = ['Mass (kg)', 'Height (m)', 'Speed (m/s)']
        return yAxisList

    def Plotter(self):
        # This is the function that excutens (is called) when the plot button
        # is pushed.
        self.temp += 1
        line = [self.temp, self.temp + 1]
        self.a.clear()
        self.a.plot(line, line)
        self.canvas.draw()


root = Tk()
window = Window(root)
window.mainloop()
