from vocabulary import Vocabulary
from netcomp import getVocabulary
from html5helpers import createComment, createTag

def createIsPartOfTag(url):
    return createTag('link', [
        ('property', 'http://schema.org/isPartOf'), 
        ('href', url)
    ])

def createLabelTag(label):
    return createTag('span', [
        ('class', 'h'),
        ('property', 'rdfs:label')
    ], label)

def createCommentTag(comment):
    return createTag('span', [
        ('property', 'rdfs:comment')
    ], comment)

def createSubClassTag(name):
    link = createTag('a', [
        ('property', 'rdfs:subClassOf'),
        ('href', 'http://schema.org/' + name)
    ], name)

    return createTag('span', [], 'Subclass of: ' + link)

def createDomainTag(name):
    link = createTag('a', [
        ('property', 'http://schema.org/domainIncludes'),
        ('href', 'http://schema.org/' + name)
    ], name)

    return createTag('span', [], 'Domain: ' + link)

def createRangeTag(name):
    link = createTag('a', [
        ('property', 'http://schema.org/rangeIncludes'),
        ('href', 'http://schema.org/' + name)
    ], name)

    return createTag('span', [], 'Range: ' + link)

def createInverseOfTag(name):
    return createTag('link', [
        ('property', 'http://schema.org/inverseOf'),
        ('href', 'http://schema.org/' + name)
    ])

def createResourceTag(type, name, tags, identLevel = 0):
    return createTag('div', [
        ('typeof', 'rdfs:' + type),
        ('resource', 'http://schema.org/' + name)
    ], '\n'.join(tags), identLevel)

def parseClass(c, voc, identLevel = 0):
    tags = []
    tags.append(createIsPartOfTag(voc.baseUrl))
    tags.append(createLabelTag(c.name))
    tags.append(createCommentTag(c.comment)) if c.comment else None

    for p in c.parents:
        tags.append(createSubClassTag(p))

    return createResourceTag('Class', c.name, tags, identLevel)

def parseProperty(p, voc, identLevel = 0):
    tags = []
    tags.append(createIsPartOfTag(voc.baseUrl))
    tags.append(createLabelTag(p.name))
    tags.append(createCommentTag(p.comment)) if p.comment else None

    for d in p.domains:
        tags.append(createDomainTag(d))

    for r in p.ranges:
        tags.append(createRangeTag(r))

    tags.append(createInverseOfTag(p.inverseOf)) if p.inverseOf else None
    return createResourceTag('Property', p.name, tags, identLevel)

def parseVocabulary(voc, filename):
    with open(filename, 'w') as out:
        out.write('<div>\n')
        out.write(createComment('netcomp extension') + '\n\n')
        out.write(createComment('CORE terms removed, see data/schema.rdf file on github:') + '\n')
        out.write(createComment('schemaorg/schemaorg/data/schema.rdfa') + '\n\n')
        out.write(createComment('EXTENSION CONTENT FOLLOWS') + '\n\n')

        out.write(createComment('Classes', 1) + '\n\n')
        for c in voc.classes:
            out.write(parseClass(voc.classes[c], voc, 1) + '\n\n')

        out.write(createComment('Properties', 1) + '\n\n')
        for p in voc.properties:
            out.write(parseProperty(voc.properties[p], voc, 1) + '\n\n')

        out.write('<div>')

if __name__ == '__main__':
    parseVocabulary(getVocabulary(), 'netcomp.rdfa')
