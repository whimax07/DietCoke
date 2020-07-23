import json
import os
import csv
import FacebookHelper as fh
from ExampleSaveAndLoad import *


def GetAndSaveTimes(sender_):
    '''This function has one arg, sender, this can be 'Me', 'All' or name of a
    person.'''
    mainDir = r"C:\Users\Max\Desktop\Parsed Message Data\Cleaned Inbox"
    newFileName = csvSave()
    if newFileName == '':
        return

    # --- Reading.
    times = []
    for root, dirs, files in fh.walklevelaround(mainDir, 1):
        if files:
            for file in files:
                baseFolder = os.path.basename(root)
                inputFile = os.path.join(mainDir, baseFolder, file)
                temp = getTimesFromOneJSON(inputFile, sender=sender_)
                if temp:
                    times.append(temp)

    # --- Wrighting.
    with open(newFileName, 'w+', newline='') as newFile:
        wr = csv.writer(newFile)
        for word in times:
            wr.writerow(word)


def getTimesFromOneJSON(inputFile, sender='All'):
    if sender == 'Me':
        sender = 'Max Whitehouse'
    times = []
    if sender == 'All':
        for message in fh.getAllMessages(inputFile):
            times.append(fh.getProperty(message, 'timestamp_ms'))
    else:
        for message in fh.getAllMessages(inputFile):
            if fh.getProperty(message, 'sender_name') == sender:
                times.append(fh.getProperty(message, 'timestamp_ms'))
    return times


if __name__ == "__main__":
    # sender_ can be 'Me', 'All' or name of a person.
    sender_ = 'Me'
    GetAndSaveTimes(sender_)
