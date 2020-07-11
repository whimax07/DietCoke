import json
import os
import csv


def walklevelaround(some_dir, level):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def RetrieveTimes(csvFile):
    times = []
    with open(csvFile) as csvFile:
        spamreader = csv.reader(csvFile, delimiter=',')
        for row in spamreader:
            times.append(row)
    times = [[int(i) for i in j] for j in times]
    times = [item for sublist in times for item in sublist]
    times.sort()
    return times