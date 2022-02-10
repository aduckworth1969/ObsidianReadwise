import os
import sys
import itertools
import requests
from dotenv import load_dotenv


def main():
    load_dotenv()


    # Create a list of files in the current directory
    validDirectory = setCurrentDirectory()
    if validDirectory:
        directory = os.getcwd()
        mdFiles = getMarkdownFilesAtDirectory(directory)
        slipboxList = getSliplist()
        missingFiles = list(set(mdFiles) - set(slipboxList))
        appendSliplist(missingFiles)
        extractText(missingFiles)
    else:
        print('Get a real OS!')
def setCurrentDirectory():
    # Identify operating system
    opSys = sys.platform
    # print(opSys)
    result = False
    # Change directory to Obsidian notes based on operating system
    if opSys == 'win32':
        os.chdir('C:/Users/aduckworth/OneDrive - SBCTC/Documents/Daily Notes/Second Brain/Second Brain/')
        result = True
    elif opSys == 'darwin':
        os.chdir("/Users/andyduckworth/Documents/Documents - Andy’s MacBook Air/Second Brain/Second Brain/Slip Box")
        result = True

    return result

def getMarkdownFilesAtDirectory(directory):
    fileList = os.listdir(directory)
    # print(fileList)

    # Create an empty list to append markdown files
    mdFiles = []
    
    # Loop through file list and append markdown files to mdFiles list
    for i in fileList:
        if i.endswith('.md'):
            mdFiles.append(i)
        else:
            pass
    
    return mdFiles

def getSliplist():
    slipFile = open('/Users/andyduckworth/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/ObsidianReadwise/slipbox.txt', 'r')
    slipbox = slipFile.readlines()
    slipboxList = [x[:-1] for x in slipbox]
    slipFile.close()
    return slipboxList

def appendSliplist(missingFiles):
    slipFileAppend = open('/Users/andyduckworth/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/ObsidianReadwise/slipbox.txt', 'a')

    for item in missingFiles:
        slipFileAppend.write(item + '\n')

    slipFileAppend.close()

def extractText(missingFiles):

    apiToken = os.getenv('apiToken')

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

if __name__ == "__main__":
    main()