import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import FacebookHelper as fh


def main():
    csvFile = r"C:\Users\Max\Desktop\Parsed Message Data" \
        + r"\Time of messages I have sent.csv"
    times = fh.RetrieveTimes(csvFile)

    times = MessWithTimeList(times)

    n, bins, patches = plt.hist(x=times, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Time')
    plt.ylabel('Total Messages Sent or Received')
    plt.title('My Very Own Histogram')

    Relabel()

    plt.show()


def MessWithTimeList(times):
    times = [i for i in times if i > 1356998400000]
    return times


def Relabel():
    locs, labels = plt.xticks()
    newLabels = []
    for time in locs:
        newLabels.append(
            datetime.fromtimestamp(time/1000).strftime('%Y-%m-%d'))
    plt.xticks(locs, newLabels, rotation=90)


if __name__ == "__main__":
    main()
