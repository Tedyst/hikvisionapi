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


xmlorig = b"""<?xml version = "1.0" encoding = "UTF-8" ?>
<DeviceInfo version = "1.0" asd = "2.0"
    xmlns = "http://www.hikvision.com/ver20/XMLSchema">
    <deviceName>DVR</deviceName>
    <deviceID>48353933-3735-3630-3433-bcad28889498</deviceID>
    <model>DS-7208HUHI-F2/N/A</model>
    <serialNumber>DS-7208HUHI-F2/N/A0820160422CCWR593756043WCVU</serialNumber>
    <macAddress>bc:ad:28:88:94:98</macAddress>
    <firmwareVersion>V3.4.88</firmwareVersion>
    <firmwareReleasedDate>build180228</firmwareReleasedDate>
    <encoderVersion>V5.0</encoderVersion>
    <encoderReleasedDate>build180126</encoderReleasedDate>
    <deviceType>IPC</deviceType>
    <telecontrolID>1</telecontrolID>
</DeviceInfo>
"""

dicti = utils.xml2dict(xmlorig)
print(dicti)
new = utils.dict2xml(dicti)
print(new)
