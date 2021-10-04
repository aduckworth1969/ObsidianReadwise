import os
import sys
import itertools
import requests
from dotenv import load_dotenv

load_dotenv()
apiToken = os.getenv('apiToken')

def identMDFiles():
    # Identify operating system
    opSys = sys.platform
    # print(opSys)

    # Change directory to Obsidian notes based on operating system
    if opSys == 'win32':
        os.chdir('C:/Users/aduckworth/OneDrive - SBCTC/Documents/Daily Notes/Second Brain/Second Brain')
    elif opSys == 'darwin':
        os.chdir('/Users/aduckworth/Library/Mobile Documents/iCloud~md~obsidian/Documents/Daily Notes')
    else:
        pass
    # print(os.getcwd())

    # Create a list of files in the current directory
    fileList = os.listdir(os.getcwd())
    # print(fileList)

    # Create an empty list to append markdown files
    mdFiles = []
    
    # Loop through file list and append markdown files to mdFiles list
    for i in fileList:
        if i.endswith('.md'):
            mdFiles.append(i)
        else:
            pass

    # print(mdFiles)

    extractText(mdFiles)

def extractText(mdFiles):
    for i in mdFiles:
        # Tag identification for text extract
        start = '#startreadwise'
        end = '#endreadwise'
        startLength = len(start)+1
        # endLength = len(end)+3
        openFile = open(i, 'r', encoding='utf8').read()
        # print(openFile)
        # Search for tag indices in text files
        startIndices = [s for s in range(len(openFile)) if openFile.startswith(start, s)]
        endIndices = [s for s in range(len(openFile)) if openFile.startswith(end, s)]
        # Loop to pull text from between tag indices and write to file
        for (s,e) in zip(startIndices,endIndices):
            # print(s,e)
            readwiseText = openFile[s+startLength:e-1]
            requests.post(
            url="https://readwise.io/api/v2/highlights/",
            headers={"Authorization": apiToken},
            json={
                "highlights": [{
                    "text": readwiseText,
                    "title": "Daily Notes for Review",
                    "author": "Andy Duckworth",
                    "source_type": "book",
                    "location_type": "page",
                    "location": 3
                    }]
                }
            )

identMDFiles()