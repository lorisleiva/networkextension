from vocabulary import Vocabulary
from netcomp import getVocabulary
from html5helpers import *
from bottle import SimpleTemplate, template

templateFolder = 'templates/'
websiteFolder = '../networkextension-website/'

def outputPage(tpl, filename, **kwargs):
    global templateFolder
    global websiteFolder

    page = template(templateFolder + tpl, kwargs)
    with open(websiteFolder + filename, 'w') as out:
        out.write(page)

def createClassPage(c, voc):
    if c.isFromSchemaOrg:
        return

    h = voc.getHierachicalInformation(c)
    outputPage('class', c.name + '.html', **{
        'title': c.name,
        'element': c,
        'breadcrumbs': h['breadcrumbs'],
        'inheritances': h['inheritances'],
    })

if __name__ == '__main__':
    voc = getVocabulary()

    outputPage('index', 'test-index.html', title='Index Title')

    for c in voc.classes:
        createClassPage(voc.classes[c], voc)
