from vocabulary import Vocabulary
from netcomp import getVocabulary
from html5helpers import *
from bottle import SimpleTemplate, template

templateFolder = 'templates/'
websiteFolder = '../networkextension-website/'

def createClassPage(c, voc):
    pass

def outputPage(tpl, filename, **kwargs):
    global templateFolder
    global websiteFolder

    page = template(templateFolder + tpl, kwargs)
    with open(websiteFolder + filename, 'w') as out:
        out.write(page)

if __name__ == '__main__':
    voc = getVocabulary()

    outputPage('index', 'test-index.html', title='title')

    for c in voc.classes:
        createClassPage(voc.classes[c], voc)
