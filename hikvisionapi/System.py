import hikvisionapi.utils as utils


def getDeviceInfo(server: utils.HikVisionServer):
    return utils.getXML(server, "/ISAPI/System/deviceInfo")
