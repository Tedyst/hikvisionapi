import hikvisionapi.utils as utils


def getDeviceInfo(server: utils.HikVisionServer):
    """
    Returns the device info as a dictionary
    """
    return utils.getXML(server, "System/deviceInfo")


def activateDevice(server: utils.HikVisionServer, password):
    """
    It is used to activate device
    """
    xml = utils.xml2dict(b'\
    <ActivateInfo version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema">\
    <password></password>\
    </ActivateInfo>')
    xml['ActivateInfo']['password'] = password
    data = utils.dict2xml(xml)

    return utils.postXML(server, "System/activate", data)


def getCapabilities(server: utils.HikVisionServer):
    """
    It is used to get device capability.
    """
    return utils.getXML(server, "System/capabilities")


def reboot(server: utils.HikVisionServer):
    """
    Reboot the device.
    """
    return utils.putXML(server, "System/reboot")


def getConfigurationData(server: utils.HikVisionServer):
    """
    Get device’s configuration data.
    """
    return utils.getXML(server, "System/configurationData")


def factoryReset(server: utils.HikVisionServer):
    """
    Get device’s configuration data.
    """
    return utils.putXML(server, "System/factoryReset")