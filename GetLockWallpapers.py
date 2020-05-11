import os
from os.path import isfile, join, getsize
from datetime import datetime
from shutil import copy2

print('-------Start-------')
print('')

# ------------------------------------------------------------------------------
# --- Decide what or if anything needs copying

# Find the date
da = datetime.now()
da = datetime.strftime(da, '%Y-%m-%d %A')
# Dir for the copy folders
lD = r'C:\Users\Max\Pictures\WinLockScreens'
onlyFolders = [f for f in os.listdir(lD) if not isfile(join(lD, f))]

# Exit if there is a folder with todays date
for i in range(len(onlyFolders)):
    if onlyFolders[i].find(da) != -1:
        print('A folder for '
              + datetime.strftime(datetime.now(), '%A the %d-%m-%Y')
              + ' already exists.')
        print('')
        print('------We Out!------')
        # Quit the program aka gtfo
        raise SystemExit

# ------------------------------------------------------------------------------
# --- Make a copy if I haven't already today

# Make the new folder
newFolder = join(lD, da)
os.mkdir(newFolder)

# The for windows spotlight photos
winLockF = (r'C:\Users\Max\AppData\Local\Packages\Microsoft.Windows.Content' +
            r'DeliveryManager_cw5n1h2txyewy\LocalState\Assets')

# Select the files bigger than 230 mB which is hopfully both all and only
# the wall papers
tbc = [f for f in os.listdir(winLockF) if getsize(join(winLockF, f)) > 230000]
for i in range(len(tbc)):
    copy2(join(winLockF, tbc[i]), join(newFolder, tbc[i] + '.jpg'))

# Give some user feed back
print('1.', 'There were ' + str(len(tbc)) + ' files copyed to:')
print('2.', '"' + newFolder + '"')

# ------------------------------------------------------------------------------

print('')
print('--------End--------')
