from vocabulary import Vocabulary

def getVocabulary():

    voc = Vocabulary('https://lorisleiva.github.io/networkextension')

    # Classes

    voc.addClass('NetworkComponent')
    voc.comment('Any type of class that falls under the netcomp extension.')
    voc.subClassOf('Thing')

    voc.addClass('EndPointComponent')
    voc.comment('Represents any type of end-points present in a computer network. E.g.: an IP address, a device or a file.')
    voc.subClassOf('NetworkComponent')

    voc.addClass('IpAddress')
    voc.comment('An host with an IP Address.')
    voc.subClassOf('EndPointComponent')

    voc.addClass('Device')
    voc.comment('A device with a Mac Address.')
    voc.subClassOf('EndPointComponent')

    voc.addClass('File')
    voc.comment('A unique file that gets transfered over the network.')
    voc.subClassOf('EndPointComponent')

    voc.addClass('Software')
    voc.comment('A software that is being or has been used by an host.')
    voc.subClassOf('EndPointComponent')

    voc.addClass('NetworkInteraction')
    voc.comment('Represents any type of interaction between various end-point components. E.g.: a Connection using HTTP.')
    voc.subClassOf('NetworkComponent')

    voc.addClass('Connection')
    voc.comment('An exchange of packages between two hosts.')
    voc.subClassOf('NetworkInteraction')

    voc.addClass('Certificate')
    voc.comment('An exchange of certificates.')
    voc.subClassOf('NetworkInteraction')

    voc.addClass('Service')
    voc.comment('A generic representation of a type of service used between two hosts.')
    voc.subClassOf('NetworkInteraction')

    voc.addClass('DHCP')
    voc.comment('A DHCP connection.')
    voc.subClassOf('Service')

    voc.addClass('DNP3')
    voc.comment('A DNP3 connection.')
    voc.subClassOf('Service')

    voc.addClass('DNS')
    voc.comment('A DNS connection.')
    voc.subClassOf('Service')

    voc.addClass('FTP')
    voc.comment('A FTP connection.')
    voc.subClassOf('Service')

    voc.addClass('HTTP')
    voc.comment('A HTTP connection.')
    voc.subClassOf('Service')

    voc.addClass('SMTP')
    voc.comment('A SMTP connection.')
    voc.subClassOf('Service')

    voc.addClass('SSH')
    voc.comment('A SSH connection.')
    voc.subClassOf('Service')

    voc.addClass('SSL')
    voc.comment('A SSL connection.')
    voc.subClassOf('Service')

    voc.addClass('NetworkNotification')
    voc.comment('Represents any system that notifies about the network\'s status.')
    voc.subClassOf('NetworkComponent')

    voc.addClass('Alert')
    voc.comment('An alert about the network\'s status.')
    voc.subClassOf('NetworkNotification')

    voc.addClass('Signature')
    voc.comment('A signature that has been detected by an IDS.')
    voc.subClassOf('NetworkNotification')

    voc.addClass('Statistic')
    voc.comment('A statistic about the network.')
    voc.subClassOf('NetworkNotification')

    # Properties

    voc.addProperty('ipv4')
    voc.comment('The IPV4 address of the host.')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Text')

    voc.addProperty('ipv6')
    voc.comment('The IPV6 address of the host.')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Text')

    return voc