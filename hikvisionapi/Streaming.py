import hikvisionapi.utils as utils


def status(server: utils.HikVisionServer):
    """
    It is used to get a device streaming status
    """
    return utils.getXML(server, "Streaming/status")


def getChannels(server: utils.HikVisionServer):
    """
    It is used to get the properties of streaming channels for the device
    """
    return utils.getXML(server, "Streaming/channels")


def putChannels(server: utils.HikVisionServer, StreamingChannelList):
    """
    It is used to update the properties of streaming channels for the device.
    A StreamingChannelList can be obtained from getChannels()
    """
    return utils.putXML(server, "Streaming/channels",
                        xmldata=StreamingChannelList)


def postChannels(server: utils.HikVisionServer, StreamingChannelList):
    """
    It is used to add a streaming channel for the device.
    A StreamingChannel can be obtained from getChannels()
    """
    return utils.postXML(server, "Streaming/channels",
                         xmldata=StreamingChannelList)


def deleteChannels(server: utils.HikVisionServer, StreamingChannelList):
    """
    It is used to add a streaming channel for the device.
    A StreamingChannel can be obtained from getChannels()
    """
    return utils.deleteXML(server, "Streaming/channels")


def getChannelByID(server: utils.HikVisionServer, ChannelID):
    """
    It is used to get the properties of a particular streaming channel for the
    device
    """
    return utils.getXML(server, "Streaming/channels/" + ChannelID)


def putChannelByID(server: utils.HikVisionServer, ChannelID, StreamingChannel):
    """
    It is used to get the properties of a particular streaming channel for the
    device
    """
    return utils.putXML(server, "Streaming/channels/" + ChannelID,
                        StreamingChannel)


def deleteChannelByID(server: utils.HikVisionServer, ChannelID):
    """
    It is used to get the properties of a particular streaming channel for the
    device
    """
    return utils.deleteXML(server, "Streaming/channels/" + ChannelID)


def getChannelRTSP(server: utils.HikVisionServer, ChannelID):
    """
    Returns the RTSP link for a channel
    """
    channel = getChannelByID(server, ChannelID)
    data = utils.xml2dict(channel)
    if data['StreamingChannel']['Transport']['ControlProtocolList']['ControlProtocol']['streamingTransport'] != "RTSP":
        return ""
    # rtsp://admin:cosica.123@192.168.1.239:554/Streaming/channels/801
    return "rtsp://" + server.user + ":" + server.password + \
        "@" + server.host + ":554/Streaming/channels/" + ChannelID
