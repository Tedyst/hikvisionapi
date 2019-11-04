import requests
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree


class HikVisionServer:
    def __init__(self, host, user, password, protocol="http", port=80):
        self.host = host
        self.protocol = protocol
        self.port = port
        self.user = user
        self.password = password
        self.address = self.protocol + "://" + self.host + ":" + str(self.port)


class Response:
    def __init__(self, statusCode=200):
        self.statusCode = statusCode


def getXML(server: HikVisionServer, ISAPI, xmldata=None):
    headers = {'Content-Type': 'application/xml'}
    if xmldata is None:
        responseRaw = requests.get(
            server.address + ISAPI,
            headers=headers,
            auth=HTTPBasicAuth(server.user, server.password))
    else:
        responseRaw = requests.post(
            server.address + ISAPI,
            data=xmldata,
            headers=headers,
            auth=HTTPBasicAuth(server.user, server.password))
    responseXML = responseRaw.text
    return responseXML
    # response=Response(statusCode=responseRaw.status_code)


class XmlDictObject(dict):
    """
    Adds object like functionality to the standard dictionary.
    """

    def __init__(self, initdict=None):
        if initdict is None:
            initdict = {}
        dict.__init__(self, initdict)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setattr__(self, item, value):
        self.__setitem__(item, value)

    def __str__(self):
        if '_text' in self:
            return self.__getitem__('_text')
        else:
            return ''

    @staticmethod
    def Wrap(x):
        """
        Static method to wrap a dictionary recursively as an XmlDictObject
        """

        if isinstance(x, dict):
            return XmlDictObject((k, XmlDictObject.Wrap(v)) for (k, v) in x.iteritems())
        elif isinstance(x, list):
            return [XmlDictObject.Wrap(v) for v in x]
        else:
            return x

    @staticmethod
    def _UnWrap(x):
        if isinstance(x, dict):
            return dict((k, XmlDictObject._UnWrap(v)) for (k, v) in x.iteritems())
        elif isinstance(x, list):
            return [XmlDictObject._UnWrap(v) for v in x]
        else:
            return x

    def UnWrap(self):
        """
        Recursively converts an XmlDictObject to a standard dictionary and returns the result.
        """

        return XmlDictObject._UnWrap(self)


def _ConvertDictToXmlRecurse(parent, dictitem):
    assert type(dictitem) is not type([])

    if isinstance(dictitem, dict):
        for (tag, child) in dictitem.iteritems():
            if str(tag) == '_text':
                parent.text = str(child)
            elif type(child) is type([]):
                # iterate through the array and convert
                for listchild in child:
                    elem = ElementTree.Element(tag)
                    parent.append(elem)
                    _ConvertDictToXmlRecurse(elem, listchild)
            else:
                elem = ElementTree.Element(tag)
                parent.append(elem)
                _ConvertDictToXmlRecurse(elem, child)
    else:
        parent.text = str(dictitem)


def ConvertDictToXml(xmldict):
    """
    Converts a dictionary to an XML ElementTree Element
    """

    roottag = xmldict.keys()[0]
    root = ElementTree.Element(roottag)
    _ConvertDictToXmlRecurse(root, xmldict[roottag])
    return root


def _ConvertXmlToDictRecurse(node, dictclass):
    nodedict = dictclass()

    if len(node.items()) > 0:
        # if we have attributes, set them
        nodedict.update(dict(node.items()))

    for child in node:
        # recursively add the element's children
        newitem = _ConvertXmlToDictRecurse(child, dictclass)
        if child.tag in nodedict:
            # found duplicate tag, force a list
            if type(nodedict[child.tag]) is type([]):
                # append to existing list
                nodedict[child.tag].append(newitem)
            else:
                # convert to list
                nodedict[child.tag] = [nodedict[child.tag], newitem]
        else:
            # only one, directly set the dictionary
            nodedict[child.tag] = newitem

    if node.text is None:
        text = ''
    else:
        text = node.text.strip()

    if len(nodedict) > 0:
        # if we have a dictionary add the text as a dictionary value (if there is any)
        if len(text) > 0:
            nodedict['_text'] = text
    else:
        # if we don't have child nodes or attributes, just set the text
        nodedict = text

    return nodedict


def ConvertXmlToDict(xml, dictclass=XmlDictObject):
    """
    Converts an XML string or ElementTree Element to a dictionary
    """

    # If a string is passed in, try to open it as a file
    if type(xml) == type(''):
        xml = ElementTree.fromstring(xml)
    elif not isinstance(xml, ElementTree.Element):
        raise TypeError("Expected ElementTree.Element or file path string")

    return dictclass({xml.tag: _ConvertXmlToDictRecurse(xml, dictclass)})


asd = """
<?xml version = "1.0" encoding = "UTF-8" ?>
<DeviceInfo version = "1.0" xmlns = "http://www.hikvision.com/ver20/XMLSchema" >
<deviceName > DVR < /deviceName >
<deviceID > 48353933-3735-3630-3433-bcad28889498 < /deviceID >
<model > DS-7208HUHI-F2/N/A < /model >
<serialNumber > DS-7208HUHI-F2/N/A0820160422CCWR593756043WCVU < /serialNumber >
<macAddress > bc: ad: 28: 88: 94: 98 < /macAddress >
<firmwareVersion > V3.4.88 < /firmwareVersion >
<firmwareReleasedDate > build 180228 < /firmwareReleasedDate >
<encoderVersion > V5.0 < /encoderVersion >
<encoderReleasedDate > build 180126 < /encoderReleasedDate >
<deviceType > IPC < /deviceType >
<telecontrolID > 1 < /telecontrolID >
</DeviceInfo >
"""
