import json
import os
import csv


def main():
    mainDir = r"C:\Users\Max\Desktop\Parsed Message Data\Cleaned Inbox"
    times = []
    for root, dirs, files in walklevelaround(mainDir, 1):
        if files:
            for file in files:
                baseFolder = os.path.basename(root)
                inputFile = os.path.join(mainDir, baseFolder, file)
                times.append(getTimes(inputFile))

    with open(r'C:\Users\Max\Desktop\Parsed Message Data\g4g.csv', 'w+',
              newline='') as newFile:
        wr = csv.writer(newFile)
        for word in times:
            wr.writerow(word)


def walklevelaround(some_dir, level):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def getTimes(inputFile):
    with open(inputFile) as dataFile:
        data = dataFile.read()
        data = json.loads(data)
    times = []
    for i in range(len(data['messages'])):
        if 'timestamp_ms' in data['messages'][i]:
            times.append(data['messages'][i]['timestamp_ms'])
    return times


if __name__ == "__main__":
    main()
