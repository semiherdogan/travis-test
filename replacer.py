#
# Vidizayn
# <semih.erdogan@vidizayn.com>
#

import os

def getEnvironmentCode(folder, prodFile, devFile, prodBranch, currentBranch):
    """Replaceses placeholders in files from MAPPING dictionary.

    Args:
        folder: root folder of given files
        prodFile: file to use if current branch is prod
        devFile: ile to use if current branch is dev
        prodBranch: prod branch
        currentBranch: current branch
    Returns:
        String
    """
    
    fileToRead = prodFile if prodBranch == currentBranch else devFile
    fileToRead = folder + '/' + fileToRead
    if os.path.isfile(fileToRead):
        with open(fileToRead, 'r', encoding='utf8') as f :
            return f.read()
    else:
        return ''

def replaceWithMapping(filePath):
    """Replaceses files placeholders from MAPPING dictionary.

    Args:
        filePath: file to replace.
    Returns:
        void
    """

    global MAPPING

    with open(filePath, 'r', encoding='utf8') as file :
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
        with open(filePath, 'w', encoding='utf8') as f:
            f.write(fileContent)

def searchFileByExtension(folderPath, ext):
    """Searches file by extension in given path recursively.

    Args:
        folderPath: root folder to search files.
        ext: file extension
    Returns:
        void
    """

    for f in os.listdir(folderPath):
        filePath = os.path.join(folderPath, f)
        if f.endswith(ext):
            replaceWithMapping(filePath)
        elif os.path.isdir(filePath):
            searchFileByExtension(filePath, ext)


CURRENT_PATH        = os.getcwd();
PUBLIC_PATH         = CURRENT_PATH + '/public'
ANALYTICS_PATH      = CURRENT_PATH + '/analytics'
PRODUCTION_BRANCH   = 'live'
CURRENT_BRACNH      = os.environ.get('TRAVIS_BRANCH')

GA_CODE = getEnvironmentCode(ANALYTICS_PATH, 'ga_prod.txt', 'ga_dev.txt', PRODUCTION_BRANCH, CURRENT_BRACNH)
OM_CODE = getEnvironmentCode(ANALYTICS_PATH, 'om_prod.txt', 'om_dev.txt', PRODUCTION_BRANCH, CURRENT_BRACNH)

MAPPING = {
    '<!-- {{ GA_CODE }} -->': GA_CODE,
    '<!-- {{ OM_CODE }} -->': OM_CODE
}

print( CURRENT_BRACNH )

searchFileByExtension(PUBLIC_PATH, '.html')
