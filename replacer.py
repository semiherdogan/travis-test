#
# Vidizayn 
#

import os
import sys

def getEnvironmentCode(prodFile, devFile, prodBranch, currentBranch):
    global ANALYTICS_PATH
    fileToRead = prodFile if prodBranch == currentBranch else devFile
    fileToRead = ANALYTICS_PATH + '/' + fileToRead
    if os.path.isfile(fileToRead):
        with open(fileToRead, 'r') as f :
            return f.read()
    else:
        return ''

def replaceWithMapping(filePath):
    global MAPPING

    with open(filePath, 'r') as file :
        fileContent = file.read()

    print('File: ' + filePath)

    willReplace = False
    for textToFind in MAPPING:
        if fileContent.find(textToFind) > -1:
            willReplace = True
            fileContent = fileContent.replace(textToFind, MAPPING[textToFind])
            print('Replaced: ' + textToFind)
        else:
            print('Not found: ' + textToFind)
    
    if willReplace :
        with open(filePath, 'w') as f:
            f.write(fileContent)

def searchFileByExtension(folderPath, ext):
    for f in os.listdir(folderPath):
        filePath = os.path.join(folderPath, f)
        if f.endswith(ext):
            replaceWithMapping(filePath)
        elif os.path.isdir(filePath):
            searchFileByExtension(filePath, ext)


CURRENT_PATH        = os.getcwd();

PUBLIC_PATH         = CURRENT_PATH + '/public'
ANALYTICS_PATH      = CURRENT_PATH + '/analytics'
PRODUCTION_BRANCH   = 'master'
CURRENT_BRACNH      = os.environ.get('TRAVIS_BRANCH')

GA_CODE = getEnvironmentCode('ga_prod.txt', 'ga_dev.txt', PRODUCTION_BRANCH, CURRENT_BRACNH)
OM_CODE = getEnvironmentCode('om_prod.txt', 'om_dev.txt', PRODUCTION_BRANCH, CURRENT_BRACNH)

MAPPING = {
    '<!-- {{ GA_CODE }} -->': GA_CODE,
    '<!-- {{ OM_CODE }} -->': OM_CODE
}

print( CURRENT_BRACNH )

searchFileByExtension(PUBLIC_PATH, '.html')
