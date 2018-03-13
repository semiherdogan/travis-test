import os
import sys

publichPath = './public'

with open('./ga_code.txt', 'r') as file :
    gaCode = file.read()

def replaceFile(fileToRepaced, textToFind, textToReplace):
    with open(fileToRepaced, 'r') as file :
        fileData = file.read()

    if fileData.find(textToFind) > -1:
        fileData = fileData.replace(textToFind, textToReplace)

        with open(fileToRepaced, 'w') as file:
            file.write(fileData)
        
        print('Replaced: ' + fileToRepaced)
    else:
        print('Not found in: ' + fileToRepaced)

def searchInfolder(folderPath):
    for fileToRepace in os.listdir(folderPath):
        
        fullPath = os.path.join(folderPath, fileToRepace)
        
        if fileToRepace.endswith('.html'):
            // replace repeatedly
            replaceFile(fullPath, gaCode)
        elif os.path.isdir(fullPath):
            searchInfolder(fullPath)


PRODUCTION_BRANCH = 'live'

print('branch: ')
print(os.environ('TRAVIS_BRANCH'))

currentBranch = 'master'
        
searchInfolder(publichPath)