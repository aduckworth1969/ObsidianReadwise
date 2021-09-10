import os
import sys

# Create an empty list to append markdown files
mdFiles = []

def identMDFiles():
    # Identify operating system
    opSys = sys.platform
    # print(opSys)

    # Change directory to Obsidian notes based on operating system
    if opSys == 'win32':
        os.chdir('C:/Users/aduckworth/iCloudDrive/iCloud~md~obsidian/Daily Notes')
    else:
        pass

    # print(os.getcwd())

    # Create a list of files in the current directory
    fileList = os.listdir(os.getcwd())
    # print(fileList)

    # Loop through file list and append markdown files to mdFiles list
    for i in fileList:
        if i.endswith('.md'):
            mdFiles.append(i)
        else:
            pass

    print(mdFiles)

identMDFiles()