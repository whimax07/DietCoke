import time
import sys
import os


def ABetterTrain(direction='RightToLeft'):
    trainPartsR2L = [
        '               o O___ _________ _________ _________  ',
        '             _][__|o| |O O O O| |O O O O| |O O O O|  ',
        '            <_______|-|_______|-|_______|-|_______|  ',
        '             /O-O-O     o   o     o   o     o   o    ']
    trainPartsL2R = [
        '  _________ _________ _________ ___O o               ',
        '  |O O O O| |O O O O| |O O O O| |o|__[]_             ',
        '  |_______|-|_______|-|_______|-|_______>            ',
        r'    o   o     o   o     o   o     O-O-O\             ']
    if direction == 'RightToLeft':
        trainParts = trainPartsL2R
    else:
        trainParts = trainPartsR2L

    # Start the print.
    for part in trainParts:
        print(part)

    cCyles = 0
    while cCyles < 100:
        # Animasion speed.
        time.sleep(0.075)

        # Clear the train from the track.
        for _ in range(len(trainParts)):
            # Move up cursor and delete whole line.
            sys.stdout.write("\x1b[1A\x1b[2K")
            sys.stdout.flush()

        # Cycle the strings so the train moves.
        if direction == 'RightToLeft':
            trainParts = [part[-1] + part[:-1] for part in trainParts]
        else:
            trainParts = [part[1:] + part[0] for part in trainParts]

        for i in range(len(trainParts)):
            sys.stdout.write(trainParts[i][:25] + "\n")  # reprint the lines
            sys.stdout.flush()

        # Exit con
        cCyles += 1

    # Clear the console because there is a bug.
    # For windows OS.
    if os.name == 'nt':
        os.system('cls')
    # For Unix
    else:
        os.system('clear')


if __name__ == "__main__":
    ABetterTrain()
