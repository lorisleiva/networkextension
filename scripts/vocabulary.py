class SemanticElement:
    def __init__(self, name, comment = None):
        self.name = name
        self.comment = comment
        self.isFromSchemaOrg = False

    def getSchemaUrl(self):
        return 'http://schema.org/' + self.name

    def getUrl(self):
        if self.isFromSchemaOrg:
            return self.getSchemaUrl()
        else:
            return '/' + self.name

class Class(SemanticElement):
    def __init__(self, name, comment = None):
        super().__init__(name, comment);
        self.parents = []
        self.properties = []
        self.rangeOf = []
        
class Property(SemanticElement):
    def __init__(self, name, comment = None):
        super().__init__(name, comment);
        self.domains = []
        self.ranges = []
        self.inverseOf = None

class Vocabulary:
    def __init__(self, baseUrl, classes = {}, properties = {}):
        self.baseUrl = baseUrl
        self.classes = classes
        self.properties = properties
        self.lastElementAdded = None

    def checkClassOrAddAsSchema(self, className):
        if className not in self.classes:
            newClass = Class(className)
            newClass.isFromSchemaOrg = True
            self.classes[className] = newClass

    def checkPropertyOrAddAsSchema(self, propertyName):
        if propertyName not in self.properties:
            newProperty = Class(propertyName)
            newProperty.isFromSchemaOrg = True
            self.classes[propertyName] = newProperty

    def addClass(self, newClassName):
        if newClassName in self.classes:
            self.classes[newClassName].isFromSchemaOrg = False
        else:
            newClass = Class(newClassName)
            self.classes[newClassName] = newClass
            self.lastElementAdded = newClass
        return self

    def subClassOf(self, className):
        self.checkClassOrAddAsSchema(className)
        parent = self.classes[className]
        self.lastElementAdded.parents.append(parent)
        return self
        
    def addProperty(self, newPropertyName):
        if newPropertyName in self.properties:
            self.properties[newPropertyName].isFromSchemaOrg = False
        else:
            newProperty = Property(newPropertyName)
            self.properties[newPropertyName] = newProperty
            self.lastElementAdded = newProperty
        return self

    def domainIncludes(self, domainName):
        self.checkClassOrAddAsSchema(domainName)
        domain = self.classes[domainName]
        self.lastElementAdded.domains.append(domain)
        domain.properties.append(self.lastElementAdded)
        return self

    def rangeIncludes(self, rangeName):
        self.checkClassOrAddAsSchema(rangeName)
        type = self.classes[rangeName]
        self.lastElementAdded.ranges.append(type)
        type.rangeOf.append(self.lastElementAdded)
        return self

    def inverseOf(self, inversePropertyName):
        self.checkPropertyOrAddAsSchema(inversePropertyName)
        inverseProperty = self.properties[inversePropertyName]
        self.lastElementAdded.inverseOf = inverseProperty
        return self

    def comment(self, comment):
        self.lastElementAdded.comment = comment
        return self

    def getHierachicalInformation(self, c):
        breadcrumbs = []
        inheritances = []

        if not c.parents:
            return {
                'breadcrumbs' : [[c]],
                'inheritances' : [c],
            }

        for parent in c.parents:
            h = self.getHierachicalInformation(parent)
            for breadcrumb in h['breadcrumbs']:
                breadcrumb.append(c)
                breadcrumbs.append(breadcrumb)
            for inheritance in h['inheritances']:
                if c not in inheritances:
                    inheritances.append(inheritance)
            inheritances.insert(0, c)

        return {
            'breadcrumbs' : breadcrumbs,
            'inheritances' : inheritances,
        }