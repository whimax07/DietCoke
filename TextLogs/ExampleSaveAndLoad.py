from tkinter import Tk
from tkinter.filedialog import asksaveasfilename, askopenfilename


Tk().withdraw()
# fileTypes need to be a list or tuples.
fileTypes = [('CSV', '*.csv')]
startdir = r"C:\Users\Max\Desktop"
# Show an "Open" dialog box and return the path to the selected file.
newFileName = asksaveasfilename(filetypes=fileTypes, initialdir=startdir,
                                defaultextension='.csv')
print(newFileName)

Tk().withdraw()
# fileTypes need to be a list or tuples.
fileTypes = [('JASON', '*.json')]
startdir = r"C:\Users\Max\Desktop"
filename = askopenfilename(filetypes=fileTypes, initialdir=startdir)
print(filename)
