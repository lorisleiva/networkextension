class SemanticElement:
    def __init__(self, name, comment = None):
        self.name = name
        self.comment = comment

    def setComment(self, comment):
        self.comment = comment
        return self

    def __repr__(self):
        return self.name + "\n\t>> " + self.comment

class Class(SemanticElement):
    def __init__(self, name, comment = None):
        super().__init__(name, comment);
        self.parents = []

    def addParent(self, className):
        self.parents.append(className)
        return self

    def __repr__(self):
        return "Class " + super().__repr__() + "\n\t>> subClassOf: " + ', '.join(self.parents)
        
class Property(SemanticElement):
    def __init__(self, name, comment = None):
        super().__init__(name, comment);
        self.domains = []
        self.ranges = []
        self.inverseOf = None

    def addDomain(self, domainName):
        self.domains.append(domainName)
        return self

    def addRange(self, rangeName):
        self.ranges.append(rangeName)
        return self

    def setInverseOf(self, inverseOf):
        self.inverseOf = inverseOf
        return self

    def __repr__(self):
        return "Property " + super().__repr__() + "\n\t>> domains: " + ', '.join(self.domains) + "\n\t>> ranges: " + ', '.join(self.ranges)

class Vocabulary:
    def __init__(self, baseUrl, classes = {}, properties = {}):
        super(Vocabulary, self).__init__()
        self.baseUrl = baseUrl
        self.classes = classes
        self.properties = properties
        self.lastElementAdded = None
        
    def addClass(self, newClassName):
        newClass = Class(newClassName)
        self.classes[newClassName] = newClass
        self.lastElementAdded = newClass
        return self

    def subClassOf(self, className):
        self.lastElementAdded.addParent(className)
        return self
        
    def addProperty(self, newPropertyName):
        newProperty = Property(newPropertyName)
        self.properties[newPropertyName] = newProperty
        self.lastElementAdded = newProperty
        return self

    def domainIncludes(self, domainName):
        self.lastElementAdded.addDomain(domainName)
        return self

    def rangeIncludes(self, rangeName):
        self.lastElementAdded.addRange(rangeName)
        return self

    def inverseOf(self, inversePropertyName):
        self.lastElementAdded.setInverseOf(inversePropertyName)
        return self

    def comment(self, comment):
        self.lastElementAdded.setComment(comment)
        return self

    def __repr__(self):
        s = "Vocabulary(" + self.baseUrl + ")\n\n"
        s += '\n\n'.join([self.classes[k].__repr__() for k in self.classes])
        s += '\n\n'
        s += '\n\n'.join([self.properties[k].__repr__() for k in self.properties])
        return s