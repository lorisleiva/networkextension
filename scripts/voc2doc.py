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
        'element': c,
        'breadcrumbs': h['breadcrumbs'],
        'inheritances': h['inheritances'],
    })

def createPropertyPage(p, voc):
    if not p.isFromSchemaOrg:
        outputPage('property', p.name + '.html', element=p)

def createClassHierarchyListItem(c, children):
    tags = []

    if c.name in children:
        linkClass = 'tbranch'
    else:
        linkClass = 'tleaf'

    tags.append(createTag('a', [
        ('href', c.getUrl()),
        ('class', linkClass)
    ], c.name))

    if c.name in children:
        subListItems = []
        for subClass in sorted(children[c.name], key=lambda x: x.name):
            li = createClassHierarchyListItem(subClass, children)
            subListItems.append(li)
        tags.append(createTag('ul', [], '\n'.join(subListItems), 0, True))

    return createTag('li', [('id', c.name)], '\n'.join(tags), 0, True)

def createClassHierarchyPage(voc):
    roots = []
    children = {}

    for className in voc.classes:
        c = voc.classes[className]

        if not c.parents and (not c.isFromSchemaOrg or c.name is 'Thing'):
            roots.append(c)

        for parent in c.parents:
            if parent.name not in children:
                children[parent.name] = []
            children[parent.name].append(c)

    rootListItem = []
    for root in sorted(roots, key=lambda x: x.name):
        rootListItem.append(createClassHierarchyListItem(root, children))
    hierarchyHtml = createTag('ul', [('class', 'no-border')], '\n'.join(rootListItem), 0, True)

    outputPage('index', 'index.html', hierarchyHtml=hierarchyHtml)

def createAllPropertiesPage(voc):
    orderedProperties = sorted(list(voc.properties.values()), key=lambda p: p.name)
    outputPage('properties', 'properties.html', properties=orderedProperties)

if __name__ == '__main__':
    voc = getVocabulary()

    createClassHierarchyPage(voc)
    createAllPropertiesPage(voc)

    for c in voc.classes:
        createClassPage(voc.classes[c], voc)

    for p in voc.properties:
        createPropertyPage(voc.properties[p], voc)
