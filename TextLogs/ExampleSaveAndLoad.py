from tkinter import Tk
from tkinter.filedialog import asksaveasfilename, askopenfilename


def csvSave(startDir=None):
    if startDir == None:
        startdir = r"C:\Users\Max\Desktop"
    Tk().withdraw()
    # fileTypes need to be a list or tuples.
    fileTypes = [('CSV', '*.csv')]
    # Show an "Save As" dialog box and return the path to the selected file.
    newFileName = asksaveasfilename(filetypes=fileTypes, initialdir=startdir,
                                    defaultextension='.csv')
    # Returns '' if saving is canceled.
    return newFileName


def jsonOpen(startDir=None):
    if startDir == None:
        startdir = r"C:\Users\Max\Desktop"
    Tk().withdraw()
    # fileTypes need to be a list or tuples.
    fileTypes = [('JASON', '*.json')]
    # Show an "Open" dialog box and return the path to the selected file.
    filename = askopenfilename(filetypes=fileTypes, initialdir=startdir)
    # Returns '' if saving is canceled.
    return filename
