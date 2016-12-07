from vocabulary import Vocabulary
from netcomp import getVocabulary
from html5helpers import *
from bottle import SimpleTemplate, template

templateFolder = 'templates/'
websiteFolder = '../networkextension-website/'

def createClassPage(c, voc):
    pass

def outputPage(page, filename):
    global websiteFolder
    with open(websiteFolder + filename, 'w') as out:
        out.write(page)

if __name__ == '__main__':
    voc = getVocabulary()

    outputPage(template(templateFolder + 'index', title='Hello World!'), 'test-index.html')

    for c in voc.classes:
        createClassPage(voc.classes[c], voc)
