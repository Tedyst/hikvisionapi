import hikvisionapi.utils
from collections import OrderedDict


def test_xml2dict():
    xmlorig = b"""<?xml version = "1.0" encoding = "UTF-8" ?>
<DeviceInfo version = "1.0" asd = "2.0"
    xmlns = "http://www.hikvision.com/ver20/XMLSchema">
    <deviceName>DVR</deviceName>
    <deviceID>someID</deviceID>
    <model>DS-7208HUHI-F2/N/A</model>
    <serialNumber>someID</serialNumber>
    <macAddress>aa:bb:cc:dd:ee:ff</macAddress>
    <firmwareVersion>V3.4.88</firmwareVersion>
    <firmwareReleasedDate>build180228</firmwareReleasedDate>
    <encoderVersion>V5.0</encoderVersion>
    <encoderReleasedDate>build180126</encoderReleasedDate>
    <deviceType>IPC</deviceType>
    <telecontrolID>1</telecontrolID>
</DeviceInfo>
"""
    dicti = hikvisionapi.utils.xml2dict(xmlorig)
    dictiorig = {'DeviceInfo': OrderedDict([('deviceName', 'DVR'), ('deviceID', 'someID'), ('model', 'DS-7208HUHI-F2/N/A'), ('serialNumber', 'someID'), ('macAddress', 'aa:bb:cc:dd:ee:ff'),
                                            ('firmwareVersion', 'V3.4.88'), ('firmwareReleasedDate', 'build180228'), ('encoderVersion', 'V5.0'), ('encoderReleasedDate', 'build180126'), ('deviceType', 'IPC'), ('telecontrolID', '1'), ('@attrs', {'version': '1.0', 'asd': '2.0'})])}
    assert dicti == dictiorig


def test_dict2xml():
    dicti = {'DeviceInfo': OrderedDict([('deviceName', 'DVR'), ('deviceID', 'someID'), ('model', 'DS-7208HUHI-F2/N/A'), ('serialNumber', 'someID'), ('macAddress', 'aa:bb:cc:dd:ee:ff'),
                                        ('firmwareVersion', 'V3.4.88'), ('firmwareReleasedDate', 'build180228'), ('encoderVersion', 'V5.0'), ('encoderReleasedDate', 'build180126'), ('deviceType', 'IPC'), ('telecontrolID', '1'), ('@attrs', {'version': '1.0', 'asd': '2.0'})])}
    xmlorig = """<?xml version = "1.0" encoding = "UTF-8" ?><DeviceInfo asd="2.0" version="1.0" xmlns="http://www.hikvision.com/ver20/XMLSchema"><deviceName>DVR</deviceName><deviceID>someID</deviceID><model>DS-7208HUHI-F2/N/A</model><serialNumber>someID</serialNumber><macAddress>aa:bb:cc:dd:ee:ff</macAddress><firmwareVersion>V3.4.88</firmwareVersion><firmwareReleasedDate>build180228</firmwareReleasedDate><encoderVersion>V5.0</encoderVersion><encoderReleasedDate>build180126</encoderReleasedDate><deviceType>IPC</deviceType><telecontrolID>1</telecontrolID></DeviceInfo>"""
    newxml = hikvisionapi.utils.dict2xml(dicti)
    print(newxml)
    assert str(xmlorig) == str(newxml)
