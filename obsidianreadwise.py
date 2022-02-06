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
        os.chdir('C:/Users/aduckworth/OneDrive - SBCTC/Documents/Daily Notes/Second Brain/Second Brain/')
    elif opSys == 'darwin':
        os.chdir("/Users/andyduckworth/Documents/Documents - Andy’s MacBook Air/Second Brain/Second Brain/Slip Box")
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

    loadProcessMdList(mdFiles)

def loadProcessMdList(mdFiles):
    slipFile = open('/Users/andyduckworth/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/ObsidianReadwise/slipbox.txt', 'r')
    slipbox = slipFile.readlines()
    slipboxList = [x[:-1] for x in slipbox]
    slipFile.close()
    missingFiles = list(set(mdFiles) - set(slipboxList))

    slipFileAppend = open('/Users/andyduckworth/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/ObsidianReadwise/slipbox.txt', 'a')

    for item in missingFiles:
        slipboxList.append(item)
        slipFileAppend.write(item + '\n')
    
    slipFileAppend.close()
   
    extractText(missingFiles)

def extractText(missingFiles):
        for i in missingFiles:
            openFile = open(i, 'r', encoding='utf8').read()
            requests.post(
            url="https://readwise.io/api/v2/highlights/",
            headers={"Authorization": apiToken},
            json={
                "highlights": [{
                    "text": i + '\n' + openFile,
                    "title": "Slip Box Review",
                    "author": "Andy Duckworth",
                    "source_type": "book",
                    "location_type": "page",
                    "location": 3
                    }]
                }
            )

identMDFiles()