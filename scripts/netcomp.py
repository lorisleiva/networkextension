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

    voc.addProperty('transactionId')
    voc.comment('A random unique identifier chosen by the actors of this transaction.')
    voc.domainIncludes('Service')
    voc.rangeIncludes('Number')

    voc.addProperty('assignedIpAddress')
    voc.comment('The IP Address assigned by the DHCP connection.')
    voc.domainIncludes('DHCP')
    voc.rangeIncludes('IpAddress')

    voc.addProperty('leaseTime')
    voc.comment('The IP Address\'s lease time.')
    voc.domainIncludes('DHCP')
    voc.rangeIncludes('Time')

    voc.addProperty('functionRequest')
    voc.comment('The name of the function message in the request.')
    voc.domainIncludes('DNP3')
    voc.rangeIncludes('Text')

    voc.addProperty('functionReply')
    voc.comment('The name of the function message in the reply.')
    voc.domainIncludes('DNP3')
    voc.rangeIncludes('Text')

    voc.addProperty('internalIndicationNumber')
    voc.comment('The response\'s "internal indication number".')
    voc.domainIncludes('DNP3')
    voc.rangeIncludes('Number')

    voc.addSchemaProperty('query', True)
    voc.comment('A sub property of instrument. The query used on this action.')
    voc.domainIncludes('DNS')
    voc.domainIncludes('SearchAction')
    voc.rangeIncludes('Text')

    voc.addProperty('qclass')
    voc.comment('The QCLASS value specifying the class of the DNS query.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Number')

    voc.addProperty('qclassName')
    voc.comment('A descriptive name for the class of the query.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Text')

    voc.addProperty('qtype')
    voc.comment('A QTYPE value specifying the type of the query.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Number')

    voc.addProperty('qtypeName')
    voc.comment('A descriptive name for the type of the query.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Text')

    voc.addProperty('rcode')
    voc.comment('The response code value in DNS response messages.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Number')

    voc.addProperty('rcodeName')
    voc.comment('A descriptive name for the response code value.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Text')

    voc.addProperty('bitQR')
    voc.comment('Whether the message is a query (False) or response (True).')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Boolean')

    voc.addProperty('bitAA')
    voc.comment('The Authoritative Answer bit for response messages specifies that the responding name server is an authority for the domain name in the question section.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Boolean')

    voc.addProperty('bitTC')
    voc.comment('The Truncation bit specifies if the message was truncated.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Boolean')

    voc.addProperty('bitRD')
    voc.comment('The Recursion Desired bit indicates to a name server to recursively purse the query.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Boolean')

    voc.addProperty('bitRA')
    voc.comment('The Recursion Available bit in a response message indicates if the name server supports recursive queries.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Boolean')

    voc.addProperty('queryAnswer')
    voc.comment('Resource descriptions in answer of the query.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Text')

    voc.addProperty('rejected')
    voc.comment('Whether the DNS query was rejected by the server.')
    voc.domainIncludes('DNS')
    voc.rangeIncludes('Boolean')

    voc.addProperty('username')
    voc.comment('User name for the current session.')
    voc.domainIncludes('HTTP')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Text')

    voc.addProperty('password')
    voc.comment('Password for the current session if captured.')
    voc.domainIncludes('HTTP')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Text')

    voc.addProperty('command')
    voc.comment('A command given by the client.')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Text')

    voc.addProperty('argument')
    voc.comment('Argument for the command if given.')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Text')

    voc.addProperty('fileAssociated')
    voc.comment('File associated with the item. E.g. for FTP, it represents the transfered file.')
    voc.domainIncludes('FTP')
    voc.domainIncludes('SMTP')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('File')

    voc.addProperty('replyCode')
    voc.comment('Reply code from the server in response to the command or request.')
    voc.domainIncludes('HTTP')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Number')

    voc.addProperty('replyMessage')
    voc.comment('Reply message from the server in response to the command or request.')
    voc.domainIncludes('HTTP')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Text')

    voc.addProperty('isPassiveMode')
    voc.comment('Whether PASV mode is toggled for the control channel.')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Boolean')

    voc.addProperty('passiveOriginatingIp')
    voc.comment('The host initiating the data connection.')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('IpAddress')

    voc.addProperty('passiveRespondingIp')
    voc.comment('The host accepting the data connection.')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('IpAddress')

    voc.addProperty('passiveRespondingPort')
    voc.comment('The port at which the acceptor is listening for the data connection.')
    voc.domainIncludes('FTP')
    voc.rangeIncludes('Number')

    voc.addSchemaProperty('httpMethod', True)
    voc.comment('An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.')
    voc.domainIncludes('HTTP')
    voc.domainIncludes('EntryPoint')
    voc.rangeIncludes('Text')

    voc.addProperty('hostHeader')
    voc.comment('Value of the HOST header.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('uri')
    voc.comment('URI used in the request.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('referrer')
    voc.comment('Value of the referrer header.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('userAgent')
    voc.comment('Value of the User-Agent header from the client.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('requestSize')
    voc.comment('Actual uncompressed content size of the request\'s body.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Number')

    voc.addProperty('responseSize')
    voc.comment('Actual uncompressed content size of the response\'s body.')
    voc.domainIncludes('HTTP')
    voc.domainIncludes('SSH')
    voc.rangeIncludes('Number')

    voc.addProperty('httpTag')
    voc.comment('Indicators of various attributes discovered and related to a particular request/response pair.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('originatingFile')
    voc.comment('Files associated with the request.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('File')

    voc.addProperty('respondingFile')
    voc.comment('Files associated with the response.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('File')

    voc.addProperty('proxyHeader')
    voc.comment('Headers that may indicate if the request was proxied.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('clientHeader')
    voc.comment('HTTP header names sent by the client.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('serverHeader')
    voc.comment('HTTP header names sent by the server.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('uriVariables')
    voc.comment('Variable names from the URI.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('cookieVariables')
    voc.comment('Variable names extracted from cookies.')
    voc.domainIncludes('HTTP')
    voc.rangeIncludes('Text')

    voc.addProperty('heloHeader')
    voc.comment('Contents of the Helo header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('heloHeader')
    voc.comment('Contents of the Helo header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('mailFromHeader')
    voc.comment('Contents of the Mail From header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('rcptToHeader')
    voc.comment('Contents of the Rcpt To header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('mailSender')
    voc.comment('Contents of the From header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('mailRecepient')
    voc.comment('Contents of the To header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('mailRecepientCc')
    voc.comment('Contents of the CC header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('replyTo')
    voc.comment('Contents of the ReplyTo header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('inReplyTo')
    voc.comment('Contents of the In-Reply-To header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('messageId')
    voc.comment('Contents of the MsgID header.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('subject')
    voc.comment('The subject of an item. E.g. For SMTP or SSL connection, it represents the content of the Subject header.')
    voc.domainIncludes('SMTP')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('lastReply')
    voc.comment('The last message the server sent to the client.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('path')
    voc.comment('The message transmission path, as extracted from the headers.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Text')

    voc.addProperty('isWebmail')
    voc.comment('Indicates if the message was sent through a webmail interface.')
    voc.domainIncludes('SMTP')
    voc.rangeIncludes('Boolean')

    voc.addProperty('connectionDirection')
    voc.comment('Direction of the connection. If the client was a local host logging into an external host, this would be OUTBOUND. INBOUND would be set for the opposite situation.')
    voc.domainIncludes('SSH')
    voc.rangeIncludes('Text')

    voc.addProperty('clientSoftware')
    voc.comment('Software string given by the client in an SSH connection.')
    voc.domainIncludes('SSH')
    voc.rangeIncludes('Text')

    voc.addProperty('serverSoftware')
    voc.comment('Software string given by the server in an SSH connection.')
    voc.domainIncludes('SSH')
    voc.rangeIncludes('Text')

    voc.addProperty('remoteLocation')
    voc.comment('The location of the remote endpoint.')
    voc.domainIncludes('SSH')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('GeoCoordinates')

    voc.addProperty('cipher')
    voc.comment('SSL/TLS cipher suite the server chose.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('sessionId')
    voc.comment('Session ID offered by the client for session resumption.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('serverSubject')
    voc.comment('Subject of the X.509 certificate offered by the server.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('serverIssuer')
    voc.comment('Subject of the signer of the X.509 certificate offered by the server.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('clientSubject')
    voc.comment('Subject of the X.509 certificate offered by the client.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('clientIssuer')
    voc.comment('Subject of the signer of the X.509 certificate offered by the client.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addSchemaProperty('validFrom', True)
    voc.comment('The date when the item becomes valid.')
    voc.domainIncludes('SSL')
    voc.domainIncludes('Demand')
    voc.domainIncludes('LocationFeatureSpecification')
    voc.domainIncludes('MonetaryAmount')
    voc.domainIncludes('Offer')
    voc.domainIncludes('OpeningHoursSpecification')
    voc.domainIncludes('Permit')
    voc.domainIncludes('PriceSpecification')
    voc.rangeIncludes('DateTime')

    voc.addSchemaProperty('validThrough', True)
    voc.comment('The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.')
    voc.domainIncludes('SSL')
    voc.domainIncludes('Demand')
    voc.domainIncludes('JobPosting')
    voc.domainIncludes('LocationFeatureSpecification')
    voc.domainIncludes('MonetaryAmount')
    voc.domainIncludes('Offer')
    voc.domainIncludes('OpeningHoursSpecification')
    voc.domainIncludes('PriceSpecification')
    voc.rangeIncludes('DateTime')

    voc.addProperty('lastAlert')
    voc.comment('Last alert that was seen during the connection.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('validationStatus')
    voc.comment('Result of certificate validation for this connection.')
    voc.domainIncludes('SSL')
    voc.rangeIncludes('Text')

    voc.addProperty('generatedAt')
    voc.comment('An absolute time indicating when the notification occurred.')
    voc.domainIncludes('NetworkNotification')
    voc.rangeIncludes('DateTime')

    voc.addProperty('alertType')
    voc.comment('The type of the Alert.')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('Text')

    voc.addProperty('message')
    voc.comment('The human readable message for the item.')
    voc.domainIncludes('Alert')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('Text')

    voc.addProperty('subMessage')
    voc.comment('The human readable sub-message for the item.')
    voc.domainIncludes('Alert')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('Text')

    voc.addProperty('sourceIp')
    voc.comment('The source address, if no connections are associated with the item.')
    voc.domainIncludes('Alert')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('IpAddress')

    voc.addProperty('destinationIp')
    voc.comment('The destination address, if no connections are associated with the item.')
    voc.domainIncludes('Alert')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('IpAddress')

    voc.addProperty('port')
    voc.comment('Associated port, if no connections are associated with the item.')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('Number')

    voc.addProperty('count')
    voc.comment('Counter or status code associated with a notification.')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('Number')

    voc.addProperty('action')
    voc.comment('Actions which have been applied to this alert.')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('Text')

    voc.addProperty('sourceIpWasDropped')
    voc.comment('Indicates if the source IP address was dropped and denied network access.')
    voc.domainIncludes('Alert')
    voc.rangeIncludes('Boolean')

    voc.addProperty('sourcePort')
    voc.comment('The port used on the source host.')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('Number')

    voc.addProperty('destinationPort')
    voc.comment('The port used on the destination host.')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('Number')

    voc.addProperty('alertAssociated')
    voc.comment('Alert associated with the signature event.')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('Alert')

    voc.addProperty('signatureCount')
    voc.comment('Numbers of signatures, from a summary count.')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('Number')

    voc.addProperty('hostCount')
    voc.comment('Numbers of hosts, from a summary count.')
    voc.domainIncludes('Signature')
    voc.rangeIncludes('Number')

    voc.addProperty('memoryUsed')
    voc.comment('Amount of memory currently in use in MB.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Number')

    voc.addProperty('packetsProcessed')
    voc.comment('Number of packets processed since the last statistic interval.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Number')

    voc.addProperty('packetsDropped')
    voc.comment('Number of packets dropped since the last statistic interval.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Number')

    voc.addProperty('statisticLag')
    voc.comment('Lag between the wall clock and packet timestamps.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Time')

    voc.addProperty('packetsLink')
    voc.comment('Number of packets seen on the link since the last statistic interval.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Number')

    voc.addProperty('bytesReceived')
    voc.comment('Number of bytes received since the last statistic interval.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Number')

    voc.addProperty('eventsProcessed')
    voc.comment('Number of events that been processed since the last statistic interval.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Number')

    voc.addProperty('eventsQueued')
    voc.comment('Number of events that been queued since the last statistic interval.')
    voc.domainIncludes('Statistic')
    voc.rangeIncludes('Number')

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