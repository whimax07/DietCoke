import json
import os


def main():
    # Read in.
    startDir = r"C:\Users\Max\Desktop\facebook-maxwhitehouse16\messages\inbox"
    endDir = r"C:\Users\Max\Desktop\facebook-maxwhitehouse16\messages" \
             + r"\Cleaned Inbox"

    for root, dirs, files in walklevelaround(startDir, 1):
        if files:
            for file in files:
                baseFolder = os.path.basename(root)
                oldFile = os.path.join(startDir, baseFolder, file)
                newFile = os.path.join(endDir, baseFolder, file)
                FixEncoding(oldFile, newFile)


def walklevelaround(some_dir, level):
    print('help')
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def FixEncoding(inputFile, outputFile):
    # I think the whitespace in open is for the type of permissions the file
    # obj has.
    with open(inputFile) as dataFile:
        data = dataFile.read()
        data = json.loads(data)
    # I am back so I have used a basic for loop to check each message for a
    # text reply and then for a reaction.
    for i in range(len(data['messages'])):
        if 'content' in data['messages'][i]:
            # Unscrambles the wacky facebook encoding.
            temp = data['messages'][i]['content'].encode('latin1') \
                .decode('UTF-8')
            # Converts the emote full text to a string with unicode-escape.
            data['messages'][i]['content'] = temp.encode('unicode-escape') \
                .decode('ASCII')

        if 'reactions' in data['messages'][i]:
            for j in range(len(data['messages'][i]['reactions'])):
                # Unscrambles the wacky facebook encoding.
                temp = data['messages'][i]['reactions'][j]['reaction'] \
                    .encode('latin1').decode('UTF-8')
                # Converts the emote full text to a string with
                # unicode-escape.
                data['messages'][i]['reactions'][j]['reaction'] \
                    = temp.encode('unicode-escape').decode('ASCII')

    os.makedirs(os.path.dirname(outputFile), exist_ok=True)
    with open(outputFile, "w+") as outputFile:
        json.dump(data, outputFile, indent=4)


if __name__ == "__main__":
    main()
