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

    voc.addProperty('uid')
    voc.comment('A unique identifier that can be used for each network component. Uids can be usefully when linked to another network management sytem like <a href="http://bro.org">Bro</a>.')
    voc.domainIncludes('NetworkComponent')
    voc.rangeIncludes('Text')

    voc.addProperty('isLocal')
    voc.comment('Determines whether the end-point component is inside the local network.')
    voc.domainIncludes('EndPointComponent')
    voc.rangeIncludes('Boolean')

    voc.addProperty('detectedAt')
    voc.comment('The date and time at which the end-point component was detected.')
    voc.domainIncludes('EndPointComponent')
    voc.rangeIncludes('DateTime')

    voc.addProperty('connectionAssociated')
    voc.comment('One or several connections associated with a particular end-point component, service or alert.')
    voc.domainIncludes('EndPointComponent')
    voc.domainIncludes('Service')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('Connection')

    voc.addProperty('ipv4')
    voc.comment('The IPV4 address of the host.')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Text')

    voc.addProperty('ipv6')
    voc.comment('The IPV6 address of the host.')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('addressCountry', True)
    voc.comment('The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.')
    voc.domainIncludes('IpAddress')
    voc.domainIncludes('GeoCoordinates')
    voc.domainIncludes('GeoShape')
    voc.domainIncludes('PostalAddress')
    voc.rangeIncludes('Country')
    voc.rangeIncludes('Text')

    voc.addProperty('macAddress')
    voc.comment('The mac address of a device, E.g. detected after a DHCP connection.')
    voc.domainIncludes('Device')
    voc.domainIncludes('DHCP')
    voc.rangeIncludes('Text')

    voc.addProperty('dhcpHostname')
    voc.comment('The value of the DHCP hostname option.')
    voc.domainIncludes('Device')
    voc.rangeIncludes('Text')

    voc.addProperty('transmitter')
    voc.comment('The host or hosts that the data sourced from.')
    voc.domainIncludes('File')
    voc.rangeIncludes('IpAddress')

    voc.addProperty('receiver')
    voc.comment('The host or hosts that the data traveled to.')
    voc.domainIncludes('File')
    voc.rangeIncludes('IpAddress')

    voc.addSchemaProperty('source', True)
    voc.comment('An identification of the source of the item. E.g. A network protocol over which a file was transfered.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')

    voc.addProperty('transactionDepth')
    voc.comment('Represent the depth of an item in a network transaction. E.g: <ul><li>For a SMTP connection: it counts the depth of the message transaction in a single connection where multiple messages were transfered.</li><li>For a HTTP connection: it represents the pipelined depth into the connection of this request/response transaction.</li><li>For a File: it depends on its source.</li></ul>')
    voc.domainIncludes('SMTP')
    voc.domainIncludes('HTTP')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')
    voc.rangeIncludes('Number')

    voc.addProperty('filename')
    voc.comment('The name of the file.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')

    voc.addProperty('filenameExtracted')
    voc.comment('The local filename of extracted file.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')

    voc.addProperty('analyzer')
    voc.comment('One or several analysis types done during file analysis.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')

    voc.addProperty('mimeType')
    voc.comment('The mime type of the file.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')

    voc.addProperty('analysisDuration')
    voc.comment('The duration the file was analyzed for.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Time')

    voc.addProperty('sendByOriginator')
    voc.comment('Indicates if the file is being sent by the originator of the connection.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Boolean')

    voc.addProperty('bytesSeen')
    voc.comment('Number of bytes provided to the analysis engine for the item.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Number')

    voc.addProperty('bytes')
    voc.comment('Total number of bytes that the item is supposed to comprised.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Number')

    voc.addProperty('bytesMissed')
    voc.comment('Number of bytes that were completely missed during the process of analysis. E.g. due to dropped packets.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Number')

    voc.addProperty('bytesOverflown')
    voc.comment('Number of \'not all-in-sequence\' bytes that were delivered to analyzers due to reassembly buffer overflow.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Number')

    voc.addProperty('parentFile')
    voc.comment('Container file from which this one was extracted as part of the file analysis.')
    voc.domainIncludes('File')
    voc.rangeIncludes('File')

    voc.addProperty('timedOut')
    voc.comment('Whether the file analysis timed out at least once for the file.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Boolean')

    voc.addProperty('md5Digest')
    voc.comment('An MD5 digest of the item\'s content.')
    voc.domainIncludes('File')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('sha1Digest')
    voc.comment('An SHA1 digest of the item\'s content.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')

    voc.addProperty('sha256Digest')
    voc.comment('An SHA256 digest of the item\'s content.')
    voc.domainIncludes('File')
    voc.rangeIncludes('Text')

    voc.addProperty('host')
    voc.comment('An IP address associated with that item. E.g.: <ul><li>For a software: it is the host that is running it.</li><li>For a certificate: it is the host that offered the certificate.</li></ul>')
    voc.domainIncludes('Software')
    voc.domainIncludes('Certificate')
    voc.rangeIncludes('IpAddress')

    voc.addProperty('hostPort')
    voc.comment('The port that the host is using.')
    voc.domainIncludes('Software')
    voc.domainIncludes('Certificate')
    voc.rangeIncludes('Number')

    voc.addProperty('softwareAssociated')
    voc.comment('One or several software associated to this host.')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Software')
    voc.inverseOf('host')

    voc.addProperty('softwareType')
    voc.comment('The type of the software. E.g. HTTP::SERVER.')
    voc.domainIncludes('Software')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('version', True)
    voc.comment('The version of the item.')
    voc.domainIncludes('Software')
    voc.domainIncludes('SSL')
    voc.domainIncludes('CreativeWork')
    voc.rangeIncludes('Text')
    voc.rangeIncludes('Number')

    voc.addProperty('startedAt')
    voc.comment('The date and time at which the interaction started.')
    voc.domainIncludes('NetworkInteraction')
    voc.rangeIncludes('DateTime')

    voc.addProperty('originatingIp')
    voc.comment('The originating ip address.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('IpAddress')
    voc.inverseOf('connectionAssociated')

    voc.addProperty('respondingIp')
    voc.comment('The responding ip address.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('IpAddress')
    voc.inverseOf('connectionAssociated')

    voc.addProperty('originatingPort')
    voc.comment('The originating endpoint\'s port.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Number')

    voc.addProperty('respondingPort')
    voc.comment('The responding endpoint\'s port.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Number')

    voc.addProperty('transportProtocol')
    voc.comment('The transport layer protocol of the connection.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Text')

    voc.addProperty('serviceAssociated')
    voc.comment('An identification of the application protocol being sent over the connection.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Service')
    voc.inverseOf('connectionAssociated')

    voc.addSchemaProperty('duration', True)
    voc.comment('The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.')
    voc.domainIncludes('Connection')
    voc.domainIncludes('Event')
    voc.domainIncludes('MediaObject')
    voc.domainIncludes('Movie')
    voc.domainIncludes('MusicRecording')
    voc.domainIncludes('MusicRelease')
    voc.rangeIncludes('Duration')
    voc.rangeIncludes('Time')

    voc.addProperty('originatingBytes')
    voc.comment('The number of payload bytes the originator sent.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Number')

    voc.addProperty('respondingBytes')
    voc.comment('The number of payload bytes the responder sent.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Number')

    voc.addSchemaProperty('status', True)
    voc.comment('The status of an item.')
    voc.domainIncludes('Connection')
    voc.domainIncludes('SSH')
    voc.rangeIncludes('Text')

    voc.addProperty('originatingPackets')
    voc.comment('The number of packets the originator sent.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Number')

    voc.addProperty('respondingPackets')
    voc.comment('The number of packets the responder sent.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Number')

    voc.addProperty('history')
    voc.comment('Records the status history of the connection.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Text')

    voc.addProperty('tunnelParents')
    voc.comment('Indicate the encapsulating parent connections used over the lifetime of this inner connection if any.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Connection')

    voc.addProperty('isWeird')
    voc.comment('Indicate if the connection has been indified as a weird in Bro.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Boolean')

    voc.addProperty('weirdName')
    voc.comment('The name of the weird (from Bro).')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Text')

    voc.addProperty('weirdInformation')
    voc.comment('More information on the weird (from Bro).')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Text')

    voc.addProperty('weirdHasAlert')
    voc.comment('Whether the weird (from Bro) has raised an alert.')
    voc.domainIncludes('Connection')
    voc.rangeIncludes('Boolean')

    voc.addProperty('certificateOffered')
    voc.comment('The certificates offered by this ip address.')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Certificate')
    voc.inverseOf('host')

    voc.addProperty('certificateSubject')
    voc.comment('The certificate\'s subject.')
    voc.domainIncludes('Certificate')
    voc.rangeIncludes('Text')

    voc.addProperty('issuerSubject')
    voc.comment('The certificate\'s issuer subject.')
    voc.domainIncludes('Certificate')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('serialNumber', True)
    voc.comment('The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.')
    voc.domainIncludes('Certificate')
    voc.domainIncludes('Demand')
    voc.domainIncludes('IndividualProduct')
    voc.domainIncludes('Offer')
    voc.rangeIncludes('Text')

    voc.addProperty('serviceRunning')
    voc.comment('One or several services running on this host.')
    voc.domainIncludes('IpAddress')
    voc.rangeIncludes('Service')

    # Thing properties for documentation purposes

    voc.addSchemaProperty('additionalType')
    voc.comment('An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the \'typeof\' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('URL')

    voc.addSchemaProperty('alternateName')
    voc.comment('An alias for the item.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('description')
    voc.comment('A description of the item.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('disambiguatingDescription')
    voc.comment('A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('image')
    voc.comment('An image of the item. This can be a <a href="http://schema.org/URL">URL</a> or a fully described <a href="http://schema.org/ImageObject">ImageObject</a>.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('ImageObject')
    voc.rangeIncludes('URL')

    voc.addSchemaProperty('mainEntityOfPage')
    voc.comment('Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See <a href="http://schema.org/docs/datamodel.html#mainEntityBackground">background notes</a> for details.<br> Inverse property: <a href="http://schema.org/mainEntity">mainEntity</a>.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('CreativeWork')
    voc.rangeIncludes('URL')

    voc.addSchemaProperty('name')
    voc.comment('The name of the item.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('potentialAction')
    voc.comment('Indicates a potential Action, which describes an idealized action in which this thing would play an \'object\' role.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('Action')

    voc.addSchemaProperty('sameAs')
    voc.comment('URL of a reference Web page that unambiguously indicates the item\'s identity. E.g. the URL of the item\'s Wikipedia page, Freebase page, or official website.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('URL')

    voc.addSchemaProperty('url')
    voc.comment('URL of the item.')
    voc.domainIncludes('Thing')
    voc.rangeIncludes('URL')

    return voc