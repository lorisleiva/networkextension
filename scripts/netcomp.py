from vocabulary import Vocabulary

def getVocabulary():

    voc = Vocabulary('https://lorisleiva.github.io/networkextension')

    # Classes

    voc.addClass('NetworkComponent')
    voc.comment('A network component is any type of class that falls under the netcomp extension.')
    voc.subClassOf('Thing')

    voc.addClass('EndPointComponent')
    voc.comment('This class represents any type of end-points present in a computer network. E.g.: an IP address, a device or a file.')
    voc.subClassOf('NetworkComponent')

    voc.addClass('IpAddress')
    voc.comment('Represent an host with an IP Address')
    voc.subClassOf('EndPointComponent')

    # Properties

    voc.addProperty('ipv4')
    voc.comment('The IPV4 address of the host')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Text')

    voc.addProperty('ipv6')
    voc.comment('The IPV6 address of the host')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Text')

    return voc