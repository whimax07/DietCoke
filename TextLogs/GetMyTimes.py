import json
import os
import csv
from tkinter import Tk
from tkinter.filedialog import asksaveasfile
import FacebookHelper as fh


def main():
    mainDir = r"C:\Users\Max\Desktop\Parsed Message Data\Cleaned Inbox"
    newFileName = r"C:\Users\Max\Desktop\Parsed Message Data" \
        + r"\Time of messages I have sent.csv"

    # --- Reading.
    times = []
    for root, dirs, files in fh.walklevelaround(mainDir, 1):
        if files:
            for file in files:
                baseFolder = os.path.basename(root)
                inputFile = os.path.join(mainDir, baseFolder, file)
                temp = getTimes(inputFile)
                if temp:
                    times.append(temp)

    # --- Wrighting.
    with open(newFileName, 'w+', newline='') as newFile:
        wr = csv.writer(newFile)
        for word in times:
            wr.writerow(word)


def getTimes(inputFile):
    with open(inputFile) as dataFile:
        data = dataFile.read()
        data = json.loads(data)

    times = []
    for i in range(len(data['messages'])):
        if 'timestamp_ms' in data['messages'][i]:
            if data['messages'][i]['sender_name'] == 'Max Whitehouse':
                times.append(data['messages'][i]['timestamp_ms'])
    return times


if __name__ == "__main__":
    main()
