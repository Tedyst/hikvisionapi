import requests
from requests.auth import HTTPBasicAuth
from lxml import etree
from collections import OrderedDict


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


def xml2dict(xml):
    tree = etree.parse(xml)
    return tree2dict(tree.getroot())


def tree2dict(node):
    """"""
    subdict = OrderedDict({})
    # iterate over the children of this element--tree.getroot
    for e in node.iterchildren():
        d = tree2dict(e)
        for k in d.keys():
            # handle duplicated tags
            if k in subdict:
                v = subdict[k]
        # use append to assert exception
                try:
                    v.append(d[k])
                    subdict.update({k: v})
                except AttributeError:
                    subdict.update({k: [v, d[k]]})
            else:
                subdict.update(d)
    if subdict:
        return {node.tag: subdict}
    else:
        return {node.tag: node.text}
