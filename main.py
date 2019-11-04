from hikvisionapi.System import getDeviceInfo
import hikvisionapi.utils as utils

server = utils.HikVisionServer("192.168.1.239", "admin", "")
xmldata = """<?xml version="1.0" encoding="utf-8"?>
    <CMSearchDescription>
        <searchID>C85AB0C7-F380-0001-E33B-A030EEB671F0</searchID>
        <trackList>
            <trackID></trackID>
        </trackList>
        <timeSpanList>
            <timeSpan>
                <startTime></startTime>
                <endTime></endTime>
            </timeSpan>
        </timeSpanList>
        <maxResults>40</maxResults>
        <searchResultPostion>0</searchResultPostion>
        <metadataList>
            <metadataDescriptor>//recordType.meta.std-cgi.com</metadataDescriptor>
        </metadataList>
    </CMSearchDescription>"""


xmlorig = getDeviceInfo(server)
print(xmlorig)
dicti = utils.ConvertXmlToDict(xmlorig)
print(dicti)
newxml = utils.ConvertDictToXml(dicti)
print(newxml)
